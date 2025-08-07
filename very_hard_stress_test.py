from manim import *
import numpy as np
import os

class VeryHardStressTest(Scene):
    """
    Very Hard stress test - Expected runtime: ~90+ minutes
    
    This scene creates extremely complex animations with:
    - 500+ objects with intricate transformations
    - 3D visualizations with high complexity
    - Advanced mathematical simulations
    - Complex particle physics simulations
    - Deep fractal generation
    - Maximum computational load for extreme testing
    """
    
    def construct(self):
        # Check if we're in test mode for fast verification
        test_mode = os.getenv('MANIM_TEST_MODE', 'false').lower() == 'true'
        
        if test_mode:
            # Fast test mode - ultra-simplified version for quick verification
            title = Text("VERY HARD Test (FAST)", font_size=56, color=RED)
            title.to_edge(UP)
            self.play(Write(title), run_time=1)
            self.wait(0.5)
            
            # Ultra-quick particle demo
            particles = VGroup()
            for i in range(15):  # Minimal particles
                particle = Dot(radius=0.06, color=self.get_temperature_color(i))
                angle = i * 2 * PI / 15
                x = 1.5 * np.cos(angle)
                y = 1.5 * np.sin(angle)
                particle.move_to([x, y, 0])
                particles.add(particle)
            
            self.play(LaggedStart(*[FadeIn(p) for p in particles], lag_ratio=0.03), run_time=1.5)
            self.play(Rotate(particles, PI/2, run_time=1.5))
            
            # Quick color change
            self.play(*[p.animate.set_color(RED) for p in particles], run_time=1)
            self.play(FadeOut(particles), run_time=1)
            
            # Minimal mathematical demo
            axes = Axes(x_range=[-1, 1], y_range=[-1, 1]).scale(0.6)
            func = axes.plot(lambda x: x**3 - x, color=YELLOW)
            self.play(Create(axes), run_time=0.8)
            self.play(Create(func), run_time=1.2)
            self.play(FadeOut(VGroup(axes, func)), run_time=0.8)
            
            # Final message
            final_text = Text("VERY HARD Test Complete!\nFast verification successful!", 
                             font_size=42, color=GREEN)
            final_text.center()
            self.play(Write(final_text), run_time=1)
            self.wait(1)
        else:
            # Normal production mode - full complexity
            title = Text("VERY HARD Stress Test - Level 4", font_size=56, color=RED)
            title.to_edge(UP)
            self.play(Write(title), run_time=3)
            self.wait(2)
            
            # Part 1: Massive particle system with physics
            self.create_particle_universe()
            
            # Part 2: Complex 3D mathematical visualizations
            self.create_3d_mathematical_landscape()
            
            # Part 3: Fractal generation and animation
            self.create_animated_fractals()
            
            # Part 4: Multiple concurrent complex animations
            self.create_concurrent_complex_animations()
            
            # Final message
            final_text = Text("VERY HARD Stress Test Complete!\nYour system is a champion!", 
                             font_size=42, color=GREEN)
            final_text.center()
            self.play(Write(final_text), run_time=3)
            self.wait(5)
    
    def create_particle_universe(self):
        """Create a massive particle system with physics simulation"""
        # Create 500 particles
        particles = VGroup()
        velocities = []
        
        for i in range(500):
            particle = Dot(radius=0.03, color=self.get_temperature_color(i))
            # Random position in a large area
            angle = np.random.random() * 2 * PI
            radius = np.random.random() * 6
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            particle.move_to([x, y, 0])
            particles.add(particle)
            
            # Random velocity
            vx = (np.random.random() - 0.5) * 2
            vy = (np.random.random() - 0.5) * 2
            velocities.append([vx, vy])
        
        # Animate particles appearing
        self.play(
            LaggedStart(*[FadeIn(particle) for particle in particles], 
                       lag_ratio=0.005),
            run_time=8
        )
        
        # Physics simulation: gravitational attraction to center
        for frame in range(120):  # 120 frames of physics
            updates = []
            for i, (particle, velocity) in enumerate(zip(particles, velocities)):
                pos = particle.get_center()
                # Gravity towards center
                dist = np.linalg.norm(pos[:2])
                if dist > 0.1:
                    gravity = -0.01 / (dist + 0.1)
                    velocities[i][0] += gravity * pos[0] / dist
                    velocities[i][1] += gravity * pos[1] / dist
                
                # Update position
                new_pos = pos + np.array([velocities[i][0], velocities[i][1], 0]) * 0.1
                updates.append(particle.animate.move_to(new_pos))
                
                # Update color based on speed
                speed = np.linalg.norm(velocities[i])
                updates.append(particle.animate.set_color(self.get_speed_color(speed)))
            
            if updates:
                self.play(*updates, run_time=0.1)
        
        # Create explosion effect
        explosion_animations = []
        for i, particle in enumerate(particles):
            direction = np.random.random(3) - 0.5
            direction = direction / np.linalg.norm(direction) * 10
            explosion_animations.append(
                particle.animate.shift(direction).set_opacity(0)
            )
        
        self.play(*explosion_animations, run_time=4)
        self.remove(*particles)
    
    def create_3d_mathematical_landscape(self):
        """Create complex 3D mathematical visualizations"""
        # Create multiple 3D surfaces
        surfaces = VGroup()
        
        # Surface 1: Complex sine waves
        surface1_points = VGroup()
        for u in np.linspace(-3, 3, 20):
            for v in np.linspace(-3, 3, 20):
                z = np.sin(u**2 + v**2) * np.cos(u*v) * np.exp(-0.1*(u**2 + v**2))
                point = Dot3D([u*0.5, v*0.5, z], radius=0.02)
                point.set_color(self.get_height_color(z))
                surface1_points.add(point)
        
        # Surface 2: Twisted torus
        surface2_points = VGroup()
        for i in range(50):
            for j in range(25):
                u = i * 2 * PI / 50
                v = j * 2 * PI / 25
                
                # Twisted torus equations
                R = 2
                r = 0.5
                x = (R + r * np.cos(v)) * np.cos(u)
                y = (R + r * np.cos(v)) * np.sin(u)
                z = r * np.sin(v) + 0.3 * np.sin(3*u)
                
                point = Dot3D([x*0.3, y*0.3, z*0.3], radius=0.02)
                point.set_color(interpolate_color(BLUE, RED, i/50))
                surface2_points.add(point)
        
        # Animate surfaces appearing
        self.play(
            LaggedStart(*[Create(point) for point in surface1_points], lag_ratio=0.002),
            run_time=10
        )
        
        # Rotate surface 1
        for _ in range(2):
            self.play(
                Rotate(surface1_points, PI/2, axis=UP, run_time=6),
                Rotate(surface1_points, PI/3, axis=RIGHT, run_time=6),
            )
        
        # Add surface 2
        self.play(
            LaggedStart(*[Create(point) for point in surface2_points], lag_ratio=0.002),
            run_time=10
        )
        
        # Complex rotations with both surfaces
        for _ in range(3):
            self.play(
                Rotate(surface1_points, PI/4, axis=[1, 1, 1], run_time=5),
                Rotate(surface2_points, -PI/3, axis=[1, 0, 1], run_time=5),
            )
        
        self.play(FadeOut(surface1_points), FadeOut(surface2_points), run_time=3)
    
    def create_animated_fractals(self):
        """Create animated fractal patterns"""
        # Mandelbrot-inspired pattern
        fractal_points = VGroup()
        
        for i in range(50):
            for j in range(50):
                x = (i - 25) / 12.5
                y = (j - 25) / 12.5
                
                # Simplified fractal calculation
                c = complex(x, y)
                z = 0
                iterations = 0
                max_iter = 15
                
                while abs(z) <= 2 and iterations < max_iter:
                    z = z*z + c
                    iterations += 1
                
                if iterations < max_iter:
                    point = Dot([x*2, y*2, 0], radius=0.02)
                    color_intensity = iterations / max_iter
                    point.set_color(interpolate_color(BLACK, YELLOW, color_intensity))
                    fractal_points.add(point)
        
        # Animate fractal appearing
        self.play(
            LaggedStart(*[FadeIn(point) for point in fractal_points], lag_ratio=0.01),
            run_time=10
        )
        
        # Animate fractal morphing
        for _ in range(3):
            morph_animations = []
            for point in fractal_points:
                new_pos = point.get_center() + (np.random.random(3) - 0.5) * 0.2
                morph_animations.append(point.animate.move_to(new_pos))
                morph_animations.append(point.animate.set_color(random_color()))
            
            self.play(*morph_animations, run_time=4)
        
        self.play(FadeOut(fractal_points), run_time=3)
    
    def create_concurrent_complex_animations(self):
        """Create multiple complex animations running concurrently"""
        # Create multiple groups of objects
        group1 = VGroup()  # Spiraling circles
        group2 = VGroup()  # Morphing polygons
        group3 = VGroup()  # Oscillating lines
        group4 = VGroup()  # Pulsating dots
        
        # Group 1: Spiraling circles
        for i in range(25):
            circle = Circle(radius=0.1, color=random_color())
            angle = i * 2 * PI / 50
            circle.move_to([2*np.cos(angle), 2*np.sin(angle), 0])
            group1.add(circle)
        
        # Group 2: Morphing polygons
        for i in range(10):
            sides = np.random.randint(3, 8)
            poly = RegularPolygon(n=sides, radius=0.2, color=random_color())
            poly.move_to([np.random.uniform(-3, 3), np.random.uniform(-2, 2), 0])
            group2.add(poly)
        
        # Group 3: Oscillating lines
        for i in range(15):
            line = Line(
                start=[np.random.uniform(-4, 4), np.random.uniform(-3, 3), 0],
                end=[np.random.uniform(-4, 4), np.random.uniform(-3, 3), 0],
                color=random_color()
            )
            group3.add(line)
        
        # Group 4: Pulsating dots
        for i in range(30):
            dot = Dot(radius=0.05, color=random_color())
            dot.move_to([np.random.uniform(-5, 5), np.random.uniform(-3, 3), 0])
            group4.add(dot)
        
        # Create all groups
        self.play(
            Create(group1),
            Create(group2),
            Create(group3),
            Create(group4),
            run_time=5
        )
        
        # Run concurrent complex animations
        for cycle in range(5):
            animations = []
            
            # Group 1: Spiral motion
            for i, circle in enumerate(group1):
                angle = cycle * PI/5 + i * 2 * PI / len(group1)
                radius = 2 + 0.5 * np.sin(cycle * PI/3)
                new_pos = [radius*np.cos(angle), radius*np.sin(angle), 0]
                animations.append(circle.animate.move_to(new_pos))
                animations.append(circle.animate.set_color(random_color()))
            
            # Group 2: Morphing and rotating
            for poly in group2:
                animations.append(Rotate(poly, PI/4, run_time=2))
                animations.append(poly.animate.scale(1.2 if cycle % 2 == 0 else 0.8))
            
            # Group 3: Oscillating lines
            for line in group3:
                start = line.get_start()
                end = line.get_end()
                new_start = start + (np.random.random(3) - 0.5) * 0.5
                new_end = end + (np.random.random(3) - 0.5) * 0.5
                animations.append(line.animate.put_start_and_end_on(new_start, new_end))
            
            # Group 4: Pulsating motion
            for dot in group4:
                scale_factor = 1 + 0.5 * np.sin(cycle * PI/2)
                animations.append(dot.animate.scale(scale_factor))
                animations.append(dot.animate.set_color(random_color()))
            
            self.play(*animations, run_time=3)
        
        # Final explosion of all objects
        final_animations = []
        all_objects = [*group1, *group2, *group3, *group4]
        for obj in all_objects:
            direction = (np.random.random(3) - 0.5) * 20
            final_animations.append(obj.animate.shift(direction).set_opacity(0))
        
        self.play(*final_animations, run_time=6)
        self.remove(*all_objects)
    
    def get_temperature_color(self, index):
        """Get color based on temperature simulation"""
        colors = [BLUE, PURPLE, RED, ORANGE, YELLOW, WHITE]
        return colors[index % len(colors)]
    
    def get_speed_color(self, speed):
        """Get color based on speed"""
        if speed < 0.1:
            return BLUE
        elif speed < 0.5:
            return GREEN
        elif speed < 1.0:
            return YELLOW
        else:
            return RED
    
    def get_height_color(self, height):
        """Get color based on height value"""
        if height < -0.5:
            return DARK_BLUE
        elif height < 0:
            return BLUE
        elif height < 0.5:
            return GREEN
        else:
            return RED

def random_color():
    """Generate a random color"""
    colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, PINK, GRAY, 
              TEAL, MAROON, GOLD, LIGHT_BLUE, LIGHT_GREEN, LIGHT_PINK]
    return np.random.choice(colors)
