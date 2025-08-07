import time
import subprocess
import sys
import os
import threading
import argparse
from datetime import datetime

def run_manim_scene(file_path, scene_name, quality="m", log_interval=15):
    """Run a manim scene and measure performance with concise logging"""
    print(f"\n{'='*60}")
    print(f"STARTING: {scene_name} (Quality: {quality})")
    print(f"File: {file_path}")
    print(f"Start: {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*60}")
    
    start_time = time.time()
    last_log_time = start_time
    
    # Set FFmpeg path
    ffmpeg_path = os.path.join(os.getcwd(), "ffmpeg-7.1.1-essentials_build", "bin")
    env = os.environ.copy()
    env["PATH"] = ffmpeg_path + ";" + env.get("PATH", "")
    
    try:
        # Run manim command
        cmd = [
            sys.executable, "-m", "manim",
            "render",
            "--quality", quality,
            "--disable_caching",
            "--verbosity", "INFO",  # Use INFO for progress updates
            file_path,
            scene_name
        ]
        
        print(f"Command: {' '.join(cmd[:4])} ... {scene_name}")
        print("Progress: Starting render...")
        
        # Run with minimal output monitoring
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            env=env,
            universal_newlines=True,
            bufsize=1
        )
        
        # Monitor with periodic time updates (non-blocking)
        frame_count = 0
        output_buffer = []
        
        def read_output():
            """Read output in a separate thread to avoid blocking"""
            try:
                for line in iter(process.stdout.readline, ''):
                    if line:
                        output_buffer.append(line)
                    else:
                        break
            except:
                pass
        
        # Start output reading thread
        output_thread = threading.Thread(target=read_output)
        output_thread.daemon = True
        output_thread.start()
        
        # Main monitoring loop with guaranteed periodic updates
        while process.poll() is None:
            current_time = time.time()
            
            # Process any buffered output
            while output_buffer:
                output = output_buffer.pop(0)
                if output and ('INFO' in output or 'frame' in output.lower()):
                    frame_count += 1
                    if frame_count % 50 == 0:  # Every 50 frames
                        elapsed = current_time - start_time
                        print(f"Progress: {elapsed/60:.1f} min - {frame_count} operations completed")
            
            # Log progress every log_interval seconds (guaranteed to run)
            if current_time - last_log_time >= log_interval:
                elapsed = current_time - start_time
                print(f"Progress: {elapsed/60:.1f} min elapsed - Still rendering...")
                last_log_time = current_time
            
            # Sleep briefly to prevent busy waiting
            time.sleep(0.5)
        
        # Wait for process to complete and output thread to finish
        process.wait()
        output_thread.join(timeout=1)
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"\n{'='*60}")
        print(f"COMPLETED: {scene_name}")
        print(f"End: {datetime.now().strftime('%H:%M:%S')}")
        print(f"Duration: {duration/60:.1f} minutes ({duration:.0f} seconds)")
        
        if process.returncode == 0:
            print("Status: SUCCESS")
            
            # Check for the specific output file
            # Manim's default output is media/videos/{script_name}/{quality}/{scene_name}.mp4
            script_name_no_ext = os.path.splitext(os.path.basename(file_path))[0]
            # Manim quality folder names are like 1080p60, 720p30 etc. Let's check for the most common ones.
            quality_map = {'l': '480p15', 'm': '720p30', 'h': '1080p60', 'p': '1440p60', 'k': '2160p60'}
            quality_folder = quality_map.get(quality, '720p30')
            
            expected_file_path = os.path.join(os.getcwd(), "media", "videos", script_name_no_ext, quality_folder, f"{scene_name}.mp4")

            if os.path.exists(expected_file_path):
                file_size = os.path.getsize(expected_file_path) / (1024*1024)  # MB
                print(f"Output: {os.path.basename(expected_file_path)} ({file_size:.1f} MB)")
                print(f"  Path: {expected_file_path}")
            else:
                print(f"Output: Video file not found at expected path: {expected_file_path}")
        else:
            print(f"Status: FAILED (Exit code: {process.returncode})")
        
        print(f"{'='*60}")
        return duration, process.returncode == 0
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return None, False

def save_report(results, start_time_str, end_time_str, test_names=None):
    """Save final test report to file"""
    # Include test difficulty in filename
    if test_names:
        if len(test_names) == 1:
            difficulty = test_names[0]
        elif len(test_names) == 4:
            difficulty = "all_tests"
        else:
            difficulty = "_".join(test_names)
    else:
        difficulty = "unknown"
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_file = f"stress_test_report_{difficulty}_{timestamp}.txt"
    
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("MANIM STRESS TEST REPORT\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Test Period: {start_time_str} to {end_time_str}\n")
            f.write("="*60 + "\n\n")
        
            f.write("RESULTS SUMMARY:\n")
            for test_name, result in results.items():
                if result["duration"] is not None:
                    actual_min = result["duration"] / 60
                    expected_min = result["expected"] / 60
                    status = "PASSED" if result["success"] else "FAILED"
                    f.write(f"{test_name:15} | {status:6} | {actual_min:6.1f}m | Expected: {expected_min:4.1f}m\n")
                else:
                    f.write(f"{test_name:15} | FAILED | Timeout/Error\n")
        
            total_time = sum(r["duration"] for r in results.values() if r["duration"] is not None)
            passed_tests = sum(1 for r in results.values() if r["success"])
            total_tests = len(results)
        
            f.write(f"\nTotal Runtime: {total_time/60:.1f} minutes\n")
            f.write(f"Success Rate: {passed_tests}/{total_tests} tests passed\n")
        
            f.write("\nSYSTEM ASSESSMENT:\n")
            if passed_tests == 3:
                f.write("EXCELLENT! System handled all stress levels successfully.\n")
            elif passed_tests == 2:
                f.write("GOOD! System handled moderate stress levels well.\n")
            elif passed_tests == 1:
                f.write("MODERATE! System handled basic stress only.\n")
            else:
                f.write("NEEDS ATTENTION! Consider system optimization.\n")
        
            # Add system info if available
            f.write("\nTEST ENVIRONMENT:\n")
            f.write(f"Python: {sys.version.split()[0]}\n")
            f.write(f"Platform: {sys.platform}\n")
            f.write(f"Working Directory: {os.getcwd()}\n")
    except (IOError, PermissionError) as e:
        print(f"\n[ERROR] Could not write report to file '{report_file}'. Reason: {e}")
        return f"FAILED_TO_SAVE_REPORT"

    return report_file

def main():
    """Main function with CLI argument parsing"""
    parser = argparse.ArgumentParser(description='Manim Stress Test Suite')
    parser.add_argument('--test', 
                       choices=['simple', 'intermediate', 'hard', 'very-hard', 'all'], 
                       default='simple',
                       help='Test to run: simple (~5min), intermediate (~20min), hard (~35min), very-hard (~90min), or all')
    parser.add_argument('--quality', choices=['l', 'm', 'h', 'p', 'k'], 
                       default='m', help='Video quality (l=low, m=medium, h=high, p=production, k=4k)')
    parser.add_argument('--log-interval', type=int, default=15, 
                       help='Logging interval in seconds (default: 15)')
    
    args = parser.parse_args()
    
    print("MANIM STRESS TEST SUITE")
    print(f"Test Selection: {args.test}")
    print(f"Quality: {args.quality}")
    print(f"Log Interval: {args.log_interval}s")
    
    start_time_str = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Start Time: {start_time_str}")
    
    results = {}
    
    # Test definitions: (file, scene_class, expected_duration_seconds)
    tests = {
        'simple': ('simple_stress_test.py', 'SimpleStressTest', 300),        # 5 min
        'intermediate': ('intermediate_stress_test.py', 'IntermediateStressTest', 1200),  # 20 min
        'hard': ('hard_stress_test.py', 'HardStressTest', 2100),             # 35 min
        'very-hard': ('very_hard_stress_test.py', 'VeryHardStressTest', 5400) # 90 min
    }
    
    # Determine which tests to run
    if args.test == 'all':
        tests_to_run = ['simple', 'intermediate', 'hard', 'very-hard']
    else:
        tests_to_run = [args.test]

    try:
        # Run selected tests
        for test_name in tests_to_run:
            if test_name in tests:
                file_path, scene_name, expected_duration = tests[test_name]
                print(f"\n*** Running {test_name.upper()} Test ***")
                
                duration, success = run_manim_scene(file_path, scene_name, args.quality, args.log_interval)
                results[test_name.capitalize()] = {
                    "duration": duration, 
                    "success": success, 
                    "expected": expected_duration
                }
                
                # Cool down between tests if running multiple
                if len(tests_to_run) > 1 and test_name != tests_to_run[-1]:
                    test_index = tests_to_run.index(test_name)
                    
                    # Extended cooling period for thermal management when running all tests
                    if len(tests_to_run) == 4 and test_index >= 1:  # After 2nd test onwards
                        print(f"\n{'='*70}")
                        print("THERMAL MANAGEMENT - Extended Cool Down")
                        print(f"{'='*70}")
                        print("Allowing system to cool for 5 minutes before next test...")
                        print("This helps prevent overheating during intensive stress testing.")
                        
                        # 5-minute countdown with progress updates
                        for remaining in range(300, 0, -30):  # Count down in 30-second intervals
                            minutes = remaining // 60
                            seconds = remaining % 60
                            if minutes > 0:
                                print(f"Cooling time remaining: {minutes}m {seconds:02d}s")
                            else:
                                print(f"Cooling time remaining: {seconds}s")
                            time.sleep(30)
                        
                        print("System cooling complete. Ready for next test.\n")
                    else:
                        # Standard cool down for other scenarios
                        print("\nCool down period: 10 seconds...")
                        time.sleep(10)
    finally:
        # Generate final report, regardless of test success or failure
        end_time_str = time.strftime('%Y-%m-%d %H:%M:%S')
        
        print("\n" + "="*70)
        print("FINAL STRESS TEST RESULTS")
        print("="*70)
        
        if not results:
            print("No tests were run or completed. No report generated.")
            return

        for test_name, result in results.items():
            if result["duration"] is not None:
                actual_min = result["duration"] / 60
                expected_min = result["expected"] / 60
                status = "PASSED" if result["success"] else "FAILED"
                print(f"{test_name:15} | {status:6} | {actual_min:6.1f}m | Expected: {expected_min:4.1f}m")
            else:
                print(f"{test_name:15} | FAILED | Timeout/Error")
        
        total_time = sum(r["duration"] for r in results.values() if r["duration"] is not None)
        passed_tests = sum(1 for r in results.values() if r["success"])
        total_tests = len(results)
        
        print(f"\nTotal Runtime: {total_time/60:.1f} minutes")
        print(f"Success Rate: {passed_tests}/{total_tests} tests")
        print(f"End Time: {end_time_str}")
        
        # Save detailed report to file
        report_file = save_report(results, start_time_str, end_time_str, tests_to_run)
        print(f"\nDetailed report saved to: {report_file}")
    


if __name__ == "__main__":
    main()
