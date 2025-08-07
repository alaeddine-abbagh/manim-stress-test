from manim import *
import numpy as np

class HardStressTest(Scene):
    """
    Hard stress test - Expected runtime: ~35 minutes
    
    This scene creates demanding animations with:
    - 800+ objects with complex transformations
    - 3D Lorenz attractor system
    - Complex mathematical simulations
    - Intensive physics simulations
    - Deep fractal generation
    - Multiple concurrent high-load animations
    - Computational load targeting 35-minute runtime
    """
    
    def construct(self):
        # Title
        title = Text("HARD Stress Test - Level 3", font_size=56, color=ORANGE)
        title.to_edge(UP)
        self.play(Write(title), run_time=3)
        self.wait(2)
        
        # Part 1: Massive particle universe with complex physics
        self.create_massive_particle_universe()
        
        # Part 2: 3D Lorenz Attractor System (NEW - High complexity)
        self.create_lorenz_attractor_system()
        
        # Part 3: Complex 3D mathematical landscapes
        self.create_complex_3d_landscapes()
        
        # Part 4: Advanced fractal generation and animation
        self.create_advanced_fractals()
        
        # Part 5: Multiple concurrent high-intensity animations
        self.create_high_intensity_concurrent_animations()
        
        # Part 6: Mathematical function visualization marathon
        self.create_mathematical_marathon()
        
        # Final message
        final_text = Text("HARD Stress Test Complete!\nSystem performed excellently!", 
                         font_size=42, color=GREEN)
        final_text.center()
        self.play(Write(final_text), run_time=3)
        self.wait(3)
    
    def create_massive_particle_universe(self):
        """Create a massive particle system with complex physics simulation"""
        # Create 400 particles (optimized for 35-minute target)
        particles = VGroup()
        velocities = []
        masses = []
        
        for i in range(400):
            mass = 0.5 + np.random.random() * 1.5  # Variable masses
            radius = 0.02 + mass * 0.02
            particle = Dot(radius=radius, color=self.get_temperature_color(i))
            
            # Random position in a very large area
            angle = np.random.random() * 2 * PI
            radius_pos = np.random.random() * 7
            x = radius_pos * np.cos(angle)
            y = radius_pos * np.sin(angle)
            particle.move_to([x, y, 0])
            particles.add(particle)
            masses.append(mass)
            
            # Random velocity with mass consideration
            vx = (np.random.random() - 0.5) * 2.5 / mass
            vy = (np.random.random() - 0.5) * 2.5 / mass
            velocities.append([vx, vy])
        
        # Animate particles appearing in waves
        wave_size = 80
        for wave in range(5):  # 5 waves of 80 particles each
            wave_particles = particles[wave*wave_size:(wave+1)*wave_size]
            self.play(
                LaggedStart(*[FadeIn(particle) for particle in wave_particles], 
                           lag_ratio=0.005),
                run_time=4
            )
        
        # Extended physics simulation with N-body interactions (100 frames)
        for frame in range(100):
            updates = []
            forces = np.zeros((len(particles), 2))
            
            # Calculate N-body forces (computationally expensive)
            for i in range(len(particles)):
                pos_i = particles[i].get_center()[:2]
                for j in range(i+1, len(particles)):
                    pos_j = particles[j].get_center()[:2]
                    diff = pos_j - pos_i
                    dist = np.linalg.norm(diff)
                    
                    if dist > 0.1:  # Avoid singularities
                        force_mag = masses[i] * masses[j] / (dist**2 + 0.01)
                        force_dir = diff / dist
                        force = force_mag * force_dir * 0.001
                        
                        forces[i] += force
                        forces[j] -= force
            
            # Update velocities and positions
            for i, (particle, velocity, mass) in enumerate(zip(particles, velocities, masses)):
                # Apply forces
                velocities[i][0] += forces[i][0] / mass
                velocities[i][1] += forces[i][1] / mass
                
                # Add central gravity
                pos = particle.get_center()
                dist = np.linalg.norm(pos[:2])
                if dist > 0.1:
                    gravity = -0.01 / (dist + 0.1)
                    velocities[i][0] += gravity * pos[0] / dist
                    velocities[i][1] += gravity * pos[1] / dist
                
                # Apply damping
                velocities[i][0] *= 0.999
                velocities[i][1] *= 0.999
                
                # Update position
                new_pos = pos + np.array([velocities[i][0], velocities[i][1], 0]) * 0.1
                updates.append(particle.animate.move_to(new_pos))
                
                # Update color and size based on speed and mass
                if frame % 3 == 0:
                    speed = np.linalg.norm(velocities[i])
                    updates.append(particle.animate.set_color(self.get_speed_color(speed)))
                    if frame % 9 == 0:  # Occasional size changes
                        new_scale = 0.8 + 0.4 * speed
                        updates.append(particle.animate.scale(new_scale))
            
            if updates:
                self.play(*updates, run_time=0.08)  # Faster individual frames
        
        # Create spectacular explosion with particle trails
        explosion_animations = []
        for i, particle in enumerate(particles):
            # Create particle trails
            trail_points = []
            for t in range(10):
                trail_point = particle.get_center() + np.random.random(3) * 0.2
                trail_points.append(trail_point)
            
            direction = (np.random.random(3) - 0.5) * 20
            explosion_animations.append(
                particle.animate.shift(direction).scale(0.1).set_opacity(0)
            )
        
        self.play(*explosion_animations, run_time=5)
        self.remove(*particles)
    
    def create_lorenz_attractor_system(self):
        """Create a 3D Lorenz attractor system with multiple attractors"""
        # Lorenz attractor parameters
        sigma = 10.0
        rho = 28.0
        beta = 8.0/3.0
        
        # Create multiple Lorenz attractors with different initial conditions
        attractors = []
        attractor_points = []
        
        initial_conditions = [
            [1.0, 1.0, 1.0], [2.0, 1.5, 0.5], [-1.0, -1.0, 1.0], 
            [1.5, -2.0, 0.8], [0.5, 2.5, -1.2], [-2.0, 0.5, 1.5]
        ]
        
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE]
        
        # Generate Lorenz attractor trajectories
        dt = 0.01
        steps = 4000  # Optimized number of steps for 35-min target
        
        for i, (x0, y0, z0) in enumerate(initial_conditions):
            points = []
            x, y, z = x0, y0, z0
            
            for step in range(steps):
                # Lorenz equations
                dx = sigma * (y - x)
                dy = x * (rho - z) - y
                dz = x * y - beta * z
                
                x += dx * dt
                y += dy * dt
                z += dz * dt
                
                # Scale and position for manim
                scaled_point = np.array([x * 0.15, y * 0.15, z * 0.1 - 2])
                points.append(scaled_point)
            
            attractor_points.append(points)
            
            # Create dots along the attractor path (every 10th point)
            attractor_dots = VGroup()
            for j in range(0, len(points), 10):
                dot = Dot(radius=0.015, color=colors[i % len(colors)])
                dot.move_to(points[j])
                attractor_dots.add(dot)
            
            attractors.append(attractor_dots)
        
        # Animate attractors appearing
        for i, attractor in enumerate(attractors):
            self.play(
                LaggedStart(*[FadeIn(dot) for dot in attractor], lag_ratio=0.002),
                run_time=8
            )
        
        # Animate the attractors evolving (computationally intensive)
        evolution_cycles = 25
        for cycle in range(evolution_cycles):
            updates = []
            
            for i, (attractor, points) in enumerate(zip(attractors, attractor_points)):
                # Shift all points along the attractor trajectory
                shift_amount = cycle * 50  # Move along the trajectory
                
                for j, dot in enumerate(attractor):
                    point_idx = (j * 10 + shift_amount) % len(points)
                    new_pos = points[point_idx]
                    updates.append(dot.animate.move_to(new_pos))
                    
                    # Color evolution based on position and time
                    color_intensity = (np.sin(cycle * 0.3 + j * 0.1) + 1) / 2
                    base_color = colors[i % len(colors)]
                    updates.append(dot.animate.set_opacity(0.3 + 0.7 * color_intensity))
            
            if updates:
                self.play(*updates, run_time=0.4)
        
        # Create connections between nearby points (very computationally expensive)
        connection_lines = VGroup()
        connection_threshold = 0.8
        
        for i, attractor1 in enumerate(attractors):
            for j, attractor2 in enumerate(attractors[i+1:], i+1):
                for dot1 in attractor1[::5]:  # Sample every 5th dot
                    for dot2 in attractor2[::5]:
                        dist = np.linalg.norm(dot1.get_center() - dot2.get_center())
                        if dist < connection_threshold:
                            line = Line(
                                dot1.get_center(), dot2.get_center(),
                                color=GRAY, stroke_width=0.5, stroke_opacity=0.3
                            )
                            connection_lines.add(line)
        
        # Animate connections appearing
        if len(connection_lines) > 0:
            self.play(
                LaggedStart(*[Create(line) for line in connection_lines], lag_ratio=0.01),
                run_time=12
            )
        
        # Final attractor dissolution
        dissolution_animations = []
        for attractor in attractors:
            for dot in attractor:
                direction = (np.random.random(3) - 0.5) * 15
                dissolution_animations.append(
                    dot.animate.shift(direction).scale(0.1).set_opacity(0)
                )
        
        for line in connection_lines:
            dissolution_animations.append(line.animate.set_opacity(0))
        
        self.play(*dissolution_animations, run_time=6)
        self.remove(*attractors, connection_lines)
    
    def create_complex_3d_landscapes(self):
        """Create multiple complex 3D mathematical landscapes"""
        
        # Landscape 1: Complex wave interference patterns
        landscape1 = VGroup()
        for i in range(30):  # Much increased
            for j in range(30):
                x = (i - 15) * 0.3
                y = (j - 15) * 0.3
                z = 0.4 * np.sin(x*2) * np.cos(y*2) + 0.2 * np.sin(x*y*0.5)
                
                cube = Cube(side_length=0.1, color=self.get_height_color(z))
                cube.move_to([x, y, z])
                landscape1.add(cube)
        
        self.play(
            LaggedStart(*[FadeIn(cube) for cube in landscape1], lag_ratio=0.002),
            run_time=12
        )
        
        # Animate complex wave patterns (40 cycles)
        for wave in range(40):
            animations = []
            t = wave * 0.15
            for i, cube in enumerate(landscape1):
                pos = cube.get_center()
                x, y = pos[0], pos[1]
                # Complex wave equations
                z = (0.4 * np.sin(x*2 + t) * np.cos(y*2 + t) + 
                     0.3 * np.sin((x+y)*1.5 - t) + 
                     0.2 * np.cos(x*y*0.5 + t*2))
                
                new_pos = [x, y, z]
                animations.append(cube.animate.move_to(new_pos))
                
                # Color based on multiple parameters
                color_val = z + 0.1 * np.sin(t + i * 0.01)
                animations.append(cube.animate.set_color(self.get_height_color(color_val)))
            
            if animations:
                self.play(*animations, run_time=0.2)
        
        # Transform into landscape 2: Fractal terrain
        landscape2 = VGroup()
        for i in range(25):
            for j in range(25):
                x = (i - 12) * 0.35
                y = (j - 12) * 0.35
                # Fractal-like height function
                z = (0.5 * np.sin(x*3) * np.cos(y*3) + 
                     0.3 * np.sin(x*6) * np.cos(y*6) + 
                     0.2 * np.sin(x*12) * np.cos(y*12))
                
                pyramid = RegularPolygon(n=3, color=self.get_height_color(z))
                pyramid.scale(0.15)
                pyramid.move_to([x, y, z])
                landscape2.add(pyramid)
        
        # Morph from cubes to pyramids
        morph_animations = []
        for i, (cube, pyramid) in enumerate(zip(landscape1, landscape2[:len(landscape1)])):
            morph_animations.append(Transform(cube, pyramid))
        
        self.play(*morph_animations, run_time=8)
        
        # Animate fractal terrain evolution (30 cycles)
        for cycle in range(30):
            animations = []
            t = cycle * 0.1
            for i, shape in enumerate(landscape1):  # Still using landscape1 after transform
                pos = shape.get_center()
                x, y = pos[0], pos[1]
                # Evolving fractal terrain
                z = (0.5 * np.sin(x*3 + t) * np.cos(y*3 + t) + 
                     0.3 * np.sin(x*6 - t*2) * np.cos(y*6 - t*2) + 
                     0.2 * np.sin(x*12 + t*3) * np.cos(y*12 + t*3))
                
                new_pos = [x, y, z]
                animations.append(shape.animate.move_to(new_pos))
                animations.append(shape.animate.set_color(self.get_height_color(z)))
                
                # Occasional rotation
                if cycle % 5 == 0:
                    animations.append(Rotate(shape, PI/6, run_time=2))
            
            if animations:
                self.play(*animations, run_time=0.25)
        
        # Final landscape explosion
        explosion_animations = []
        for shape in landscape1:
            direction = (np.random.random(3) - 0.5) * 25
            explosion_animations.append(
                shape.animate.shift(direction).scale(0.1).set_opacity(0)
            )
        
        self.play(*explosion_animations, run_time=6)
        self.remove(landscape1)
    
    def create_advanced_fractals(self):
        """Create advanced animated fractal patterns with deep recursion"""
        # Create complex fractal-like branching structures
        def create_complex_branch(start_pos, angle, length, depth, group, branch_factor=3):
            if depth <= 0 or length < 0.05:
                return
            
            end_pos = start_pos + length * np.array([np.cos(angle), np.sin(angle), 0])
            
            # Create branch with varying thickness
            thickness = depth * 0.5
            line = Line(start_pos, end_pos, 
                       color=self.get_temperature_color(depth * 15),
                       stroke_width=thickness)
            group.add(line)
            
            if depth > 1:
                # Create multiple branches (increased complexity)
                for i in range(branch_factor):
                    branch_angle = angle + (i - branch_factor//2) * PI/4
                    length_factor = 0.65 + 0.1 * np.sin(i)
                    create_complex_branch(end_pos, branch_angle, 
                                        length * length_factor, depth - 1, group, branch_factor)
        
        # Create multiple complex fractal systems
        fractal_systems = VGroup()
        
        # System 1: Deep tree fractals
        for tree_num in range(6):  # Optimized from 8
            tree = VGroup()
            angle_offset = tree_num * 2 * PI / 6
            start_x = 4 * np.cos(angle_offset)
            start_y = 4 * np.sin(angle_offset)
            create_complex_branch([start_x, start_y, 0], PI/2 + angle_offset, 2.0, 6, tree)  # Optimized recursion depth
            fractal_systems.add(tree)
        
        # System 2: Mandelbrot-inspired patterns
        mandelbrot_points = VGroup()
        for i in range(80):
            for j in range(80):
                # Scaled coordinates for Mandelbrot set
                x = (i - 50) * 0.04
                y = (j - 50) * 0.04
                c = complex(x, y)
                z = 0
                
                # Calculate Mandelbrot iterations (computationally expensive)
                iterations = 0
                max_iterations = 50
                while abs(z) < 2 and iterations < max_iterations:
                    z = z*z + c
                    iterations += 1
                
                if iterations < max_iterations:
                    # Create point with color based on iteration count
                    color_intensity = iterations / max_iterations
                    point = Dot(radius=0.015, 
                              color=interpolate_color(BLUE, RED, color_intensity))
                    point.move_to([x*8, y*8, 0])
                    mandelbrot_points.add(point)
        
        # Animate fractal systems appearing
        for i, system in enumerate(fractal_systems):
            self.play(
                LaggedStart(*[Create(branch) for branch in system], lag_ratio=0.05),
                run_time=6
            )
        
        # Animate Mandelbrot set appearing
        self.play(
            LaggedStart(*[FadeIn(point) for point in mandelbrot_points], lag_ratio=0.001),
            run_time=15
        )
        
        # Complex fractal evolution cycles
        for cycle in range(15):  # Optimized cycles
            animations = []
            
            # Rotate and transform tree fractals
            for i, system in enumerate(fractal_systems):
                rotation_angle = PI/12 * (1 + np.sin(cycle * 0.3 + i))
                animations.append(Rotate(system, rotation_angle, run_time=3))
                
                # Change colors of branches
                for branch in system:
                    new_color = interpolate_color(RED, BLUE, np.sin(cycle * 0.2 + i * 0.5))
                    animations.append(branch.animate.set_color(new_color))
            
            # Animate Mandelbrot points
            for i, point in enumerate(mandelbrot_points[::5]):  # Sample points
                scale_factor = 1 + 0.3 * np.sin(cycle * 0.4 + i * 0.01)
                animations.append(point.animate.scale(scale_factor))
                
                # Shift colors
                color_shift = (cycle * 0.1) % 1.0
                new_color = interpolate_color(BLUE, RED, (color_shift + i * 0.001) % 1.0)
                animations.append(point.animate.set_color(new_color))
            
            if animations:
                self.play(*animations, run_time=2.5)
        
        # Final fractal explosion
        explosion_animations = []
        
        # Explode tree fractals
        for system in fractal_systems:
            for branch in system:
                direction = (np.random.random(3) - 0.5) * 20
                explosion_animations.append(
                    branch.animate.shift(direction).scale(0.1).set_opacity(0)
                )
        
        # Explode Mandelbrot points
        for point in mandelbrot_points:
            direction = (np.random.random(3) - 0.5) * 30
            explosion_animations.append(
                point.animate.shift(direction).scale(0.1).set_opacity(0)
            )
        
        self.play(*explosion_animations, run_time=8)
        self.remove(*fractal_systems, mandelbrot_points)
    
    def create_high_intensity_concurrent_animations(self):
        """Create multiple high-intensity animations running concurrently"""
        # Create massive groups of objects for maximum computational load
        group1 = VGroup()  # Complex rotating shapes
        group2 = VGroup()  # Morphing polygons with variable sides
        group3 = VGroup()  # Dynamic oscillating lines
        group4 = VGroup()  # Pulsating and orbiting dots
        group5 = VGroup()  # NEW: Bezier curve networks
        group6 = VGroup()  # NEW: Mathematical function plots
        
        # Group 1: Complex rotating shapes (35 objects)
        for i in range(35):
            sides = 3 + i % 8
            shape = RegularPolygon(n=sides, radius=0.1 + 0.05 * np.sin(i), color=random_color())
            angle = i * 2 * PI / 35
            radius = 1.5 + 0.5 * np.cos(i * 0.3)
            shape.move_to([radius*np.cos(angle), radius*np.sin(angle), 0])
            group1.add(shape)
        
        # Group 2: Morphing polygons (30 objects)
        for i in range(30):
            sides = np.random.randint(3, 12)
            poly = RegularPolygon(n=sides, radius=0.15, color=random_color())
            x = np.random.uniform(-4, 4)
            y = np.random.uniform(-3, 3)
            poly.move_to([x, y, 0])
            group2.add(poly)
        
        # Group 3: Dynamic oscillating lines (40 objects)
        for i in range(40):
            start = [np.random.uniform(-5, 5), np.random.uniform(-4, 4), 0]
            end = [np.random.uniform(-5, 5), np.random.uniform(-4, 4), 0]
            line = Line(start=start, end=end, color=random_color(), stroke_width=2)
            group3.add(line)
        
        # Group 4: Pulsating and orbiting dots (80 objects)
        for i in range(80):
            dot = Dot(radius=0.04, color=random_color())
            angle = i * 2 * PI / 80
            radius = 3 + np.sin(i * 0.2)
            dot.move_to([radius*np.cos(angle), radius*np.sin(angle), 0])
            group4.add(dot)
        
        # Group 5: Bezier curve networks (30 curves)
        for i in range(30):
            # Create complex Bezier curves
            points = []
            for j in range(4):  # 4 control points per curve
                point = [np.random.uniform(-6, 6), np.random.uniform(-4, 4), 0]
                points.append(point)
            
            # Create curved path
            curve_points = []
            for t in np.linspace(0, 1, 20):
                # Cubic Bezier formula
                p = ((1-t)**3 * np.array(points[0]) + 
                     3*(1-t)**2*t * np.array(points[1]) + 
                     3*(1-t)*t**2 * np.array(points[2]) + 
                     t**3 * np.array(points[3]))
                curve_points.append(p)
            
            curve = VMobject(color=random_color(), stroke_width=1.5)
            curve.set_points_as_corners(curve_points)
            group5.add(curve)
        
        # Group 6: Mathematical function plots (25 functions)
        for i in range(25):
            # Create various mathematical function plots
            func_points = []
            for x in np.linspace(-4, 4, 50):
                if i % 5 == 0:
                    y = 0.5 * np.sin(x * (i+1)) * np.cos(x * 0.5)
                elif i % 5 == 1:
                    y = 0.3 * x * np.sin(x * 2) / (x + 0.1)
                elif i % 5 == 2:
                    y = 0.4 * np.exp(-x**2/4) * np.sin(x * 3)
                elif i % 5 == 3:
                    y = 0.2 * (x**2 - 2) * np.cos(x * 1.5)
                else:
                    y = 0.3 * np.sin(x) / (x**2 + 1) * np.cos(x * 2)
                
                func_points.append([x, y, 0])
            
            plot = VMobject(color=random_color(), stroke_width=1)
            plot.set_points_as_corners(func_points)
            plot.shift([i * 0.2, i * 0.1, 0])  # Slight offset for each plot
            group6.add(plot)
        
        # Create all groups in waves for dramatic effect
        wave_groups = [group1, group2, group3, group4, group5, group6]
        for i, group in enumerate(wave_groups):
            self.play(
                LaggedStart(*[Create(obj) for obj in group], lag_ratio=0.02),
                run_time=5
            )
        
        # Run intensive concurrent animations (12 cycles)
        for cycle in range(12):
            animations = []
            
            # Group 1: Complex spiral and rotation
            for i, shape in enumerate(group1):
                angle = cycle * PI/3 + i * 2 * PI / len(group1)
                radius = 1.5 + 0.8 * np.sin(cycle * 0.4 + i * 0.1)
                new_pos = [radius*np.cos(angle), radius*np.sin(angle), 0]
                animations.append(shape.animate.move_to(new_pos))
                animations.append(Rotate(shape, PI/6, run_time=2))
                
                if cycle % 3 == 0:
                    animations.append(shape.animate.set_color(random_color()))
                    new_scale = 0.8 + 0.4 * np.sin(cycle * 0.5 + i * 0.2)
                    animations.append(shape.animate.scale(new_scale))
            
            # Group 2: Morphing and complex transformations
            for poly in group2:
                animations.append(Rotate(poly, PI/5, run_time=2.5))
                scale_factor = 1 + 0.5 * np.sin(cycle * 0.6)
                animations.append(poly.animate.scale(scale_factor))
                
                if cycle % 4 == 0:
                    new_x = np.random.uniform(-4, 4)
                    new_y = np.random.uniform(-3, 3)
                    animations.append(poly.animate.move_to([new_x, new_y, 0]))
            
            # Group 3: Dynamic line oscillations
            for line in group3:
                start = line.get_start()
                end = line.get_end()
                
                # Complex oscillation pattern
                offset1 = np.array([np.sin(cycle * 0.7) * 0.5, np.cos(cycle * 0.5) * 0.3, 0])
                offset2 = np.array([np.cos(cycle * 0.8) * 0.4, np.sin(cycle * 0.6) * 0.5, 0])
                
                new_start = start + offset1 + (np.random.random(3) - 0.5) * 0.2
                new_end = end + offset2 + (np.random.random(3) - 0.5) * 0.2
                
                animations.append(line.animate.put_start_and_end_on(new_start, new_end))
            
            # Group 4: Complex orbital motion
            for i, dot in enumerate(group4):
                # Multiple orbital frequencies
                angle1 = cycle * PI/4 + i * 2 * PI / len(group4)
                angle2 = cycle * PI/6 + i * PI / len(group4)
                radius1 = 2 + np.sin(cycle * 0.3 + i * 0.05)
                radius2 = 0.5 * np.cos(cycle * 0.5 + i * 0.1)
                
                x = radius1 * np.cos(angle1) + radius2 * np.cos(angle2)
                y = radius1 * np.sin(angle1) + radius2 * np.sin(angle2)
                
                animations.append(dot.animate.move_to([x, y, 0]))
                
                # Pulsating effect
                pulse_scale = 1 + 0.3 * np.sin(cycle * 0.8 + i * 0.2)
                animations.append(dot.animate.scale(pulse_scale))
            
            # Group 5: Bezier curve deformation
            for curve in group5[::2]:  # Every other curve to manage complexity
                # Slight rotation and color change
                animations.append(Rotate(curve, PI/12, run_time=2))
                if cycle % 5 == 0:
                    animations.append(curve.animate.set_color(random_color()))
            
            # Group 6: Function plot evolution
            for plot in group6[::3]:  # Every third plot
                shift_amount = [np.sin(cycle * 0.4) * 0.2, np.cos(cycle * 0.3) * 0.1, 0]
                animations.append(plot.animate.shift(shift_amount))
            
            if animations:
                self.play(*animations, run_time=2)
        
        # Spectacular final implosion
        implosion_animations = []
        all_objects = [*group1, *group2, *group3, *group4, *group5, *group6]
        
        for obj in all_objects:
            # All objects converge to center then explode outward
            animations.append(obj.animate.move_to(ORIGIN).scale(0.1))
        
        self.play(*implosion_animations, run_time=4)
        
        # Final explosion
        explosion_animations = []
        for obj in all_objects:
            direction = (np.random.random(3) - 0.5) * 25
            explosion_animations.append(
                obj.animate.shift(direction).set_opacity(0)
            )
        
        self.play(*explosion_animations, run_time=6)
        self.remove(*all_objects)
    
    def create_mathematical_marathon(self):
        """Create an intensive mathematical visualization marathon"""
        # Mathematical sequence 1: Fourier series approximations
        fourier_functions = VGroup()
        for n in range(1, 16):  # 15 different approximations
            points = []
            for x in np.linspace(-PI, PI, 100):
                # Square wave Fourier series
                y = 0
                for k in range(1, n+1):
                    y += (4/PI) * np.sin((2*k-1)*x) / (2*k-1)
                y *= 0.5  # Scale for display
                points.append([x, y, 0])
            
            fourier_curve = VMobject(color=interpolate_color(RED, BLUE, n/16))
            fourier_curve.set_points_as_corners(points)
            fourier_curve.shift([0, n*0.3, 0])  # Stack them
            fourier_functions.add(fourier_curve)
        
        # Mathematical sequence 2: Parametric equations
        parametric_curves = VGroup()
        for i in range(12):
            points = []
            for t in np.linspace(0, 4*PI, 200):
                # Various parametric equations
                if i % 5 == 0:
                    # Rose curves
                    k = 2 + i // 5
                    r = np.cos(k * t)
                    x = r * np.cos(t)
                    y = r * np.sin(t)
                elif i % 5 == 1:
                    # Lissajous curves
                    a = 1 + i * 0.2
                    b = 2 + i * 0.1
                    x = np.sin(a * t)
                    y = np.sin(b * t)
                elif i % 5 == 2:
                    # Hypotrochoids
                    R = 3
                    r = 1 + i * 0.1
                    d = 0.5 + i * 0.05
                    x = (R-r)*np.cos(t) + d*np.cos((R-r)*t/r)
                    y = (R-r)*np.sin(t) - d*np.sin((R-r)*t/r)
                elif i % 5 == 3:
                    # Spiral of Archimedes
                    a = 0.1 + i * 0.02
                    x = a * t * np.cos(t)
                    y = a * t * np.sin(t)
                else:
                    # Cardioid
                    a = 1 + i * 0.1
                    x = a * (2*np.cos(t) - np.cos(2*t))
                    y = a * (2*np.sin(t) - np.sin(2*t))
                
                points.append([x*0.3, y*0.3, 0])
            
            curve = VMobject(color=random_color())
            curve.set_points_as_corners(points)
            curve.shift([i*0.5, 0, 0])
            parametric_curves.add(curve)
        
        # Create Fourier series
        self.play(
            LaggedStart(*[Create(curve) for curve in fourier_functions], lag_ratio=0.1),
            run_time=10
        )
        
        # Animate Fourier evolution
        for cycle in range(10):
            animations = []
            for i, curve in enumerate(fourier_functions):
                # Shift and scale based on harmonic number
                shift_amount = [np.sin(cycle * 0.3 + i * 0.1) * 0.2, 0, 0]
                animations.append(curve.animate.shift(shift_amount))
                
                # Color evolution
                new_color = interpolate_color(RED, BLUE, (cycle * 0.1 + i * 0.05) % 1.0)
                animations.append(curve.animate.set_color(new_color))
            
            self.play(*animations, run_time=1.5)
        
        # Transform to parametric curves
        transform_animations = []
        for i, (fourier, param) in enumerate(zip(fourier_functions, parametric_curves[:len(fourier_functions)])):
            transform_animations.append(Transform(fourier, param))
        
        self.play(*transform_animations, run_time=8)
        
        # Animate parametric curve evolution
        for cycle in range(10):
            animations = []
            for i, curve in enumerate(fourier_functions):  # Still using fourier_functions after transform
                # Complex transformations
                scale_factor = 1 + 0.3 * np.sin(cycle * 0.4 + i * 0.2)
                animations.append(curve.animate.scale(scale_factor))
                
                rotation_angle = PI/8 * np.sin(cycle * 0.3 + i * 0.1)
                animations.append(Rotate(curve, rotation_angle, run_time=2))
                
                if cycle % 4 == 0:
                    animations.append(curve.animate.set_color(random_color()))
            
            self.play(*animations, run_time=2)
        
        # Final mathematical dissolution
        dissolution_animations = []
        for curve in fourier_functions:
            direction = (np.random.random(3) - 0.5) * 20
            dissolution_animations.append(
                curve.animate.shift(direction).scale(0.1).set_opacity(0)
            )
        
        self.play(*dissolution_animations, run_time=5)
        self.remove(*fourier_functions)
    
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
