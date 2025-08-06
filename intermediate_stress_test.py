from manim import *
import numpy as np

class IntermediateStressTest(Scene):
    """
    Intermediate stress test - Expected runtime: ~20 minutes
    
    This scene creates more complex animations with:
    - 200 objects with complex transformations
    - Multiple 3D elements
    - Particle systems
    - Complex mathematical visualizations
    - Higher frame rate and longer duration
    """
    
    def construct(self):
        # Title
        title = Text("Intermediate Stress Test - Level 2", font_size=48, color=ORANGE)
        title.to_edge(UP)
        self.play(Write(title), run_time=2)
        self.wait(1)
        
        # Create a moderate particle system
        particles = VGroup()
        for i in range(80):
            particle = Dot(radius=0.05, color=random_color())
            # Random position in a circle
            angle = i * 2 * PI / 200
            radius = 3 * np.sqrt(np.random.random())
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            particle.move_to([x, y, 0])
            particles.add(particle)
        
        # Animate particles appearing with complex timing
        self.play(
            LaggedStart(*[FadeIn(particle) for particle in particles], 
                       lag_ratio=0.02),
            run_time=4
        )
        self.wait(1)
        
        # Rotation and scaling animation
        for _ in range(2):
            self.play(
                Rotate(particles, PI/2, run_time=3),
                particles.animate.scale(1.2),
            )
            self.play(
                particles.animate.scale(0.8),
                run_time=2
            )
        
        # Create a spiral motion
        self.play(
            *[particle.animate.shift(
                [0.1*np.cos(i*0.1 + self.renderer.time), 
                 0.1*np.sin(i*0.1 + self.renderer.time), 0]
            ) for i, particle in enumerate(particles)],
            run_time=5
        )
        
        # Mathematical visualization: Fourier series
        self.play(FadeOut(particles))
        
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE},
        )
        
        # Create multiple sine waves
        waves = VGroup()
        for n in range(1, 10, 2):  # Fewer harmonics
            wave = axes.plot(
                lambda x, n=n: (4/PI) * np.sin(n*x) / n,
                color=interpolate_color(RED, YELLOW, n/20)
            )
            waves.add(wave)
        
        # Fourier series sum
        fourier_sum = axes.plot(
            lambda x: sum((4/PI) * np.sin(n*x) / n for n in range(1, 10, 2)),
            color=WHITE,
            stroke_width=6
        )
        
        self.play(Create(axes), run_time=2)
        
        # Animate waves building up
        for wave in waves:
            self.play(Create(wave), run_time=0.5)
        
        self.wait(1)
        self.play(Create(fourier_sum), run_time=4)
        self.wait(2)
        
        # 3D visualization
        self.remove(*self.mobjects)
        
        # Create 3D surface
        surface_points = []
        for u in np.linspace(-2, 2, 20):
            for v in np.linspace(-2, 2, 20):
                x = u
                y = v
                z = 0.5 * (np.sin(u**2 + v**2) * np.exp(-0.1*(u**2 + v**2)))
                surface_points.append([x, y, z])
        
        # Create dots for 3D surface
        surface_dots = VGroup()
        for point in surface_points[::2]:  # Skip some points for performance
            dot = Dot3D(point=point, color=color_gradient([BLUE, GREEN, RED], len(surface_points))[surface_points.index(point) % len(surface_points)])
            surface_dots.add(dot)
        
        # Animate 3D surface
        self.play(
            LaggedStart(*[Create(dot) for dot in surface_dots], lag_ratio=0.01),
            run_time=6
        )
        
        # Rotate the 3D surface
        for _ in range(1):
            self.play(
                Rotate(surface_dots, PI/3, axis=UP, run_time=4),
                Rotate(surface_dots, PI/4, axis=RIGHT, run_time=4),
            )
        
        # Complex color animations
        self.play(
            *[dot.animate.set_color(random_color()) for dot in surface_dots],
            run_time=3
        )
        
        # Final cleanup
        self.play(FadeOut(Group(*self.mobjects)), run_time=3)
        
        # Final message
        final_text = Text("Intermediate Stress Test Complete!", font_size=36, color=GREEN)
        self.play(Write(final_text), run_time=2)
        self.wait(3)

def random_color():
    """Generate a random color"""
    colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, PINK, GRAY, TEAL, MAROON]
    return np.random.choice(colors)
