# Manim Animation Stress Test Suite

A comprehensive stress testing suite for evaluating system performance using Manim (Mathematical Animation Engine) animations with varying computational complexity levels.

## 📋 Table of Contents

- [Overview](#overview)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Test Levels](#test-levels)
- [Usage](#usage)
- [Command Line Parameters](#command-line-parameters)
- [Output Files](#output-files)
- [Environment Details](#environment-details)
- [Troubleshooting](#troubleshooting)
- [Technical Details](#technical-details)

## 🎯 Overview

This stress test suite is designed to evaluate system performance through computationally intensive Manim animations. It provides four difficulty levels, each targeting different runtime durations and computational loads.

**Target System**: Intel i7 Asus Zenbook Pro 16X  
**Framework**: Manim Community Edition  
**Language**: Python 3.12+


## 🔧 Installation

### 1. Install Python 3.12+
Download from [python.org](https://www.python.org/downloads/)

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg
**Windows:**
- Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
- Extract and add to system PATH

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

### 4. Verify Installation
```bash
python -c "import manim; print('Manim installed successfully')"
ffmpeg -version
```

## 🎮 Test Levels

| Level | Name | Expected Runtime | Complexity | Description |
|-------|------|-----------------|------------|-------------|
| 1 | **Simple** | ~5 minutes | Low | Basic animations, 100 objects |
| 2 | **Intermediate** | ~20 minutes | Medium | Moderate complexity, 400+ objects |
| 3 | **Hard** | ~35 minutes | High | 3D Lorenz attractors, N-body physics, 800+ objects |
| 4 | **Very Hard** | ~90+ minutes | Extreme | Maximum complexity, 1000+ objects, deep recursion |

### Test Components by Level

#### Simple Test
- Basic geometric animations
- Simple transformations
- Color transitions
- ~100 animated objects

#### Intermediate Test
- Physics simulations
- 3D visualizations
- Complex transformations
- ~400 animated objects

#### Hard Test ⭐ 
- **3D Lorenz Attractor System** (8 attractors, 8000 steps each)
- **N-body Particle Physics** (800 particles, gravitational interactions)
- **Advanced Mandelbrot Fractals** (100×100 computation grid)
- **High-Intensity Concurrent Animations** (285+ objects across 6 groups)
- **Mathematical Function Marathon** (Fourier series, parametric equations)

#### Very Hard Test
- Extreme computational load
- Deep fractal recursion
- Complex mathematical simulations
- Maximum object counts
- Extended animation sequences

## 🚀 Usage

### Quick Start
```bash
# Run a single test
python run_stress_tests.py --test simple

# Run all tests (WARNING: 2+ hours total runtime)
python run_stress_tests.py --test all

# Run with high quality
python run_stress_tests.py --test hard --quality h
```

### Recommended Testing Sequence
1. **Start with Simple**: Verify basic functionality
2. **Try Intermediate**: Test moderate load handling
3. **Run Hard**: Evaluate high-performance capabilities
4. **Very Hard**: Only for extreme stress testing

## ⚙️ Command Line Parameters

### Required Parameters
None (defaults to simple test)

### Optional Parameters

#### `--test` (Test Selection)
- **Choices**: `simple`, `intermediate`, `hard`, `very-hard`, `all`
- **Default**: `simple`
- **Description**: Select which test(s) to run

```bash
python run_stress_tests.py --test hard
```

#### `--quality` (Video Quality)
- **Choices**: `l`, `m`, `h`, `p`, `k`
- **Default**: `m`
- **Description**: Video output quality
  - `l` = Low (480p15fps) - Fastest
  - `m` = Medium (720p30fps) - Default
  - `h` = High (1080p60fps) - Recommended
  - `p` = Production (1440p60fps) - High quality
  - `k` = 4K (2160p60fps) - Maximum quality

```bash
python run_stress_tests.py --test simple --quality h
```

#### `--log-interval` (Logging Frequency)
- **Type**: Integer (seconds)
- **Default**: `15`
- **Range**: 5-60 seconds
- **Description**: Progress logging interval

```bash
python run_stress_tests.py --test intermediate --log-interval 10
```

### Example Commands

```bash
# Basic usage
python run_stress_tests.py

# High quality single test
python run_stress_tests.py --test hard --quality h --log-interval 10

# All tests with production quality (WARNING: Very long runtime)
python run_stress_tests.py --test all --quality p --log-interval 30

# Quick low-quality test for debugging
python run_stress_tests.py --test simple --quality l --log-interval 5
```

## 📁 Output Files

### Video Files
- **Location**: `media/videos/{test_name}/{quality}/`
- **Format**: MP4
- **Naming**: `{TestClassName}.mp4`

#### Example Structure
```
media/
└── videos/
    ├── simple_stress_test/
    │   └── 720p30/
    │       └── SimpleStressTest.mp4
    ├── hard_stress_test/
    │   └── 1080p60/
    │       └── HardStressTest.mp4
    └── ...
```

### Report Files
- **Location**: Root directory
- **Format**: Text file (.txt)
- **Naming**: `stress_test_report_{difficulty}_{timestamp}.txt`

#### Report Filename Examples
- `stress_test_report_simple_20250806_183745.txt`
- `stress_test_report_hard_20250806_194532.txt`
- `stress_test_report_all_tests_20250806_201015.txt`

#### Report Contents
- Test execution summary
- Runtime statistics
- Success/failure status
- System performance assessment
- Environment information
- Detailed timing breakdowns

## 🌍 Environment Details

### Python Dependencies
```
manim==0.18.0
numpy>=1.21.0
```

### System Information Captured
- Python version
- Platform details
- Working directory
- FFmpeg configuration
- System memory usage
- CPU utilization

### Environment Variables
The test suite automatically configures:
- `PAGER=cat` (for command output)
- FFmpeg path detection
- Manim verbosity settings

## 🔧 Troubleshooting

### Common Issues

#### FFmpeg Not Found
**Error**: `FFmpeg not found in PATH`
**Solution**: 
1. Install FFmpeg
2. Add to system PATH
3. Restart terminal

#### Permission Errors
**Error**: `Permission denied writing report`
**Solution**: 
1. Run from writable directory
2. Check file permissions
3. Run as administrator if needed

#### Memory Issues
**Error**: `Out of memory` or slow performance
**Solution**:
1. Close other applications
2. Use lower quality settings (`--quality l`)
3. Run tests individually instead of `--test all`

#### Rendering Failures
**Error**: Test fails with exit code 1
**Solution**:
1. Check Manim installation: `python -c "import manim"`
2. Verify dependencies: `pip install -r requirements.txt`
3. Check FFmpeg: `ffmpeg -version`

### Performance Optimization

#### For Slower Systems
```bash
# Use low quality and longer logging intervals
python run_stress_tests.py --test simple --quality l --log-interval 30
```

#### For High-End Systems
```bash
# Use maximum quality and frequent logging
python run_stress_tests.py --test hard --quality k --log-interval 5
```

## 📊 Technical Details

### Computational Complexity Analysis

#### Simple Test: O(n) - Linear
- Basic animations with minimal computational overhead
- Single-threaded operations
- Memory usage: ~100MB

#### Intermediate Test: O(n²) - Quadratic
- Physics simulations with object interactions
- 3D transformations
- Memory usage: ~500MB

#### Hard Test: O(n³) - Cubic
- **N-body physics**: O(n²) particle interactions
- **Lorenz attractors**: O(n) with high constant factor
- **Mandelbrot computation**: O(n²) with deep iteration
- Memory usage: ~1-2GB

#### Very Hard Test: O(n⁴) - Polynomial
- Maximum complexity algorithms
- Deep recursive computations
- Memory usage: ~2-4GB

### Performance Metrics

The test suite measures:
- **Total runtime**
- **Frames per second** (rendering speed)
- **Memory consumption**
- **CPU utilization**
- **Disk I/O** (video file writing)

### Hardware Scaling

Expected performance scaling by CPU:
- **Intel i5/AMD Ryzen 5**: Simple + Intermediate recommended
- **Intel i7/AMD Ryzen 7**: All tests except Very Hard
- **Intel i9/AMD Ryzen 9**: All tests including Very Hard

## 📈 Interpreting Results

### Success Criteria
- **PASSED**: Test completed without errors
- **FAILED**: Test encountered errors or timeouts
- **Runtime**: Actual vs expected duration comparison

### Performance Assessment
- **EXCELLENT**: All tests pass, runtime ≤ expected
- **GOOD**: Most tests pass, runtime slightly over expected
- **MODERATE**: Basic tests pass, advanced tests struggle
- **NEEDS ATTENTION**: Multiple failures, consider system optimization

## 📞 Support

For issues or questions:
1. Check this README
2. Verify system requirements
3. Review troubleshooting section
4. Check Manim Community documentation

---

**Last Updated**: August 2025  
**Version**: 2.0  
**Compatibility**: Python 3.8+, Manim Community 0.18+
