#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


# COLOR_MAP in constants.py
'''
often used templates:
播放前生成图形
Circle(color=PURPLE_A)
Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
Rectangle(height=2, width=3)
Ellipse(width=3, height=1, color=RED)
CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
Annulus(inner_radius=.5, outer_radius=1, color=BLUE)

生成以后调整初始位置
.move_to(UP+LEFT)
.surround(square)
.shift(2*DOWN+2*RIGHT)
.next_to(circle,DOWN+LEFT)

开始播放
self.add(图形)
self.play(动画(图形))
动画：
FadeIn()
Rotating()
GrowArrow(arrow)
GrowFromCenter()

'''
class Learn(Scene):
    def construct(self):
        # circle = Circle(color=PURPLE_A)
        # square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        # square.move_to(UP+LEFT)
        # circle.surround(square)
        # rectangle = Rectangle(height=2, width=3)
        # ellipse=Ellipse(width=3, height=1, color=RED)
        # ellipse.shift(2*DOWN+2*RIGHT)
        # pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        # arrow = Arrow(LEFT,UP)
        # arrow.next_to(circle,DOWN+LEFT)
        # rectangle.next_to(arrow,DOWN+LEFT)
        # ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        # ring.next_to(ellipse, RIGHT)

        # self.add(pointer)
        # self.play(FadeIn(square))
        # self.play(Rotating(square),FadeIn(circle))
        # self.play(GrowArrow(arrow))
        # self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

        square1 = Square(fill_color=RED, fill_opacity=1, color=GOLD_A)
        square2 = Square(fill_color=YELLOW, fill_opacity=1, color=GOLD_A)
        square3 = Square(fill_color=GREEN, fill_opacity=1, color=GOLD_A)
        square4 = Square(fill_color=BLUE, fill_opacity=1, color=GOLD_A)
        square1.move_to([-2,0,1])
        square2.move_to([-1,0,2])
        square3.move_to([0,0,0])
        square4.move_to([1,0,-1])

        self.play(GrowFromCenter(square1), GrowFromCenter(square2), GrowFromCenter(square3), GrowFromCenter(square4))
        

        self.wait()

class Shapes(Scene):
    # A few simple shapes
    def construct(self):
        circle = Circle()
        square = Square()
        vector = Vector()
        line=Line()
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))
        da = DoubleArrow(np.array([4,-2,0]),np.array([1,1,0]))
        e = Elbow()

        self.add(e)
        self.add(line) # 不带动画直接添加
        self.add(vector)
        self.add(da)
        
        
        self.play(ShowCreation(square))
        self.play(Transform(da,square))
        
        self.wait()

class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        example_text = TextMobject(
            "This is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )

        self.add(example_text)
        self.wait()
        self.play(Transform(example_text, example_tex))
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

# See old_projects folder for many, many more
