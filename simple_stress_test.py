from manim import *
import numpy as np
import os

class SimpleStressTest(Scene):
    """
    Simple stress test - Expected runtime: ~5 minutes
    
    This scene creates basic geometric transformations with moderate complexity.
    It includes:
    - 50 circles with basic animations
    - Simple mathematical functions
    - Basic text animations
    - Moderate frame count for reasonable render time
    """
    
    def construct(self):
        # Check if we're in test mode for fast verification
        test_mode = os.getenv('MANIM_TEST_MODE', 'false').lower() == 'true'
        
        if test_mode:
            # Fast test mode - reduced complexity for quick verification
            title = Text("Simple Test (FAST)", font_size=48, color=BLUE)
            title.to_edge(UP)
            self.play(Write(title), run_time=0.5)
            self.wait(0.5)
            
            # Create fewer circles for fast test
            circles = VGroup()
            for i in range(3):  # Reduced from 10x5 to 3x2
                for j in range(2):
                    circle = Circle(radius=0.3, color=random_color())
                    circle.move_to([i*1.5 - 1.5, j*1.0 - 0.5, 0])
                    circles.add(circle)
        else:
            # Normal test mode - full complexity
            title = Text("Simple Stress Test - Level 1", font_size=48, color=BLUE)
            title.to_edge(UP)
            self.play(Write(title))
            self.wait(1)
            
            # Create a grid of circles with animations
            circles = VGroup()
            for i in range(10):
                for j in range(5):
                    circle = Circle(radius=0.2, color=random_color())
                    circle.move_to([i*0.8 - 3.6, j*0.6 - 1.2, 0])
                    circles.add(circle)
        
        # Animate circles appearing
        if test_mode:
            self.play(LaggedStart(*[Create(circle) for circle in circles], lag_ratio=0.05), run_time=1)
            self.wait(0.2)
            
            # Quick rotate
            self.play(Rotate(circles, PI/2, run_time=1))
            self.wait(0.2)
            
            # Quick scale animation
            self.play(circles.animate.scale(1.3), run_time=0.5)
            self.play(circles.animate.scale(0.8), run_time=0.5)
            self.wait(0.2)
            
            # Quick color transformation
            self.play(
                *[circle.animate.set_color(YELLOW) for circle in circles],
                run_time=1
            )
            self.wait(0.2)
        else:
            self.play(LaggedStart(*[Create(circle) for circle in circles], lag_ratio=0.1))
            self.wait(1)
            
            # Rotate all circles
            self.play(Rotate(circles, PI, run_time=3))
            self.wait(1)
            
            # Scale animation
            self.play(circles.animate.scale(1.5), run_time=2)
            self.play(circles.animate.scale(0.7), run_time=2)
            self.wait(1)
            
            # Color transformation
            self.play(
                *[circle.animate.set_color(YELLOW) for circle in circles],
                run_time=3
            )
            self.wait(1)
        
        if test_mode:
            # Simple quick finish for test mode
            self.play(FadeOut(circles), run_time=1)
            final_text = Text("Simple Test Complete!", font_size=36, color=GREEN)
            self.play(Write(final_text), run_time=1)
            self.wait(0.5)
        else:
            # Mathematical function plot
            axes = Axes(
                x_range=[-3, 3, 1],
                y_range=[-2, 2, 1],
                axis_config={"color": GREEN},
            ).scale(0.7)
            
            func = axes.plot(lambda x: np.sin(2*x) * np.cos(x), color=RED)
            
            self.play(Transform(circles, axes))
            self.wait(1)
            self.play(Create(func), run_time=3)
            self.wait(2)
            
            # Final transformation
            self.play(FadeOut(Group(*self.mobjects)))
            
            # Final message
            final_text = Text("Simple Stress Test Complete!", font_size=36, color=GREEN)
            self.play(Write(final_text))
            self.wait(2)

def random_color():
    """Generate a random color"""
    colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, PINK, GRAY]
    return np.random.choice(colors)
