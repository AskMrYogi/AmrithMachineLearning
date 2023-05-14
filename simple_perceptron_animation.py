from manim import *
from numpy import array
import random

class ShowAnimation(Scene):

    def construct(self):


        #show input / output
        self.data_scene()

        self.clear()

        self.create_network()
        self.clear()


    def data_scene(self):
        train_inputs = array([[0, 0, 0], [1, 1, 1], [1, 0, 1], [0, 1, 1], [0, 1, 0]])
        output = array([[0], [1], [1], [0], [0]])

        inp_txt = Text("Input", font_size=20).move_to([-5, 3, 0])
        inp_matrix = Matrix(train_inputs, v_buff=0.6, h_buff=0.6, bracket_h_buff=SMALL_BUFF, bracket_v_buff=SMALL_BUFF)
        inp_matrix.next_to(inp_txt,DOWN)
        out_txt = Text("Expected\nOutput", font_size=20).next_to(inp_txt, RIGHT).shift(0.5 * RIGHT)
        out_matrix = Matrix(output, v_buff=0.6, h_buff=0.6, bracket_h_buff=SMALL_BUFF, bracket_v_buff=SMALL_BUFF)
        out_matrix.next_to(inp_matrix)

        inp_rectangles = VGroup()
        out_rectangles = VGroup()
        inp_texts = VGroup()
        inp_arrows = VGroup()
        out_texts = VGroup()
        out_arrows = VGroup()

        for i in range(len(train_inputs)):
            input_rectangle = SurroundingRectangle(inp_matrix.get_rows()[i], color="Green", buff=0.1)
            #rectangles.add(input_rectangle)
            output_rectangle = SurroundingRectangle(out_matrix.get_rows()[i], color="Yellow", buff=0.1)
            inp_rectangles.add(input_rectangle)

            input_text = Text("Input Value", font_size=15).next_to(input_rectangle, LEFT)
            input_arrow = Arrow(input_text.get_right(), input_rectangle.get_left(), buff=1)
            inp_texts.add(input_text)
            inp_arrows.add(input_arrow)


            out_rectangles.add(output_rectangle)
            out_text = Text("Target", font_size=15).next_to(output_rectangle, RIGHT)
            out_arrow = Arrow(out_text.get_left(), output_rectangle.get_right(), buff=1)
            out_texts.add(out_text)
            out_arrows.add(out_arrow)

        animations = [
            FadeIn(inp_txt),
            Create(inp_matrix),
            FadeIn(out_txt),
            Create(out_matrix),
        ]
        self.play(*animations, lag_ratio=0.5)

        for i in range(len(inp_rectangles)):
            if i==0:
                self.play(
                    Create(inp_rectangles[i]),
                    Create(out_rectangles[i]),
                    FadeIn(inp_texts[i]),
                    GrowArrow(inp_arrows[i]),
                    FadeIn(out_texts[i]),
                    GrowArrow(out_arrows[i])
                )
            else:
                animations = [
                    ReplacementTransform(inp_rectangles[i - 1],inp_rectangles[i]),
                    ReplacementTransform(out_rectangles[i - 1], out_rectangles[i]),
                    ReplacementTransform(inp_texts[i - 1],inp_texts[i]),
                    ReplacementTransform(inp_arrows[i - 1], inp_arrows[i]),
                    ReplacementTransform(out_texts[i - 1], out_texts[i]),
                    ReplacementTransform(out_arrows[i - 1], out_arrows[i]),
                ]
                self.play(AnimationGroup(*animations))

        self.wait()


    def create_network(self):

        inp_1_circle = Circle(radius=.5, color="BLUE")
        inp_2_circle = Circle(radius=.5, color="BLUE")
        inp_3_circle = Circle(radius=.5, color="BLUE")

        circles_group = VGroup(inp_1_circle, inp_2_circle, inp_3_circle).arrange(DOWN, buff=0.5)

        inp_1_circle.move_to([-5,3,0])
        inp_2_circle.next_to(inp_1_circle,DOWN)
        inp_3_circle.next_to(inp_2_circle, DOWN)
        start_position = [-5, 3, 0]


        train_inputs = array([[0, 0, 0], [1, 1, 1], [1, 0, 1], [0, 1, 1], [0, 1, 0]])
        inp_matrix=Matrix(train_inputs,
            v_buff=0.6,
            h_buff=0.6,
            bracket_h_buff=SMALL_BUFF,
            bracket_v_buff=SMALL_BUFF
            )
        inp_matrix.next_to(inp_3_circle,DOWN)
        fir_1 = SurroundingRectangle(inp_matrix.get_rows()[0],color="Green",buff=.1)

        animations = [
            # Create(inp_1_circle),
            # Create(inp_2_circle),
            # Create(inp_3_circle),
            FadeIn(circles_group),
            FadeIn(inp_matrix),
            Create(fir_1)
        ]

        self.play(AnimationGroup(*animations,lag_ratio=.5))

        animations_1 = [
            ApplyMethod(inp_matrix.get_rows()[0][0].move_to, inp_1_circle),
            ApplyMethod(inp_matrix.get_rows()[0][1].move_to, inp_2_circle),
            ApplyMethod(inp_matrix.get_rows()[0][2].move_to, inp_3_circle),
        ]
        self.play(AnimationGroup(*animations_1,lag_ratio=.5))
        animations_2 = [
            FadeOut(fir_1),
            FadeOut(inp_matrix)

        ]
        self.play(AnimationGroup(*animations_2,lag_ratio=.5))


        new_pos =[-4,0,0]

        animations_3=[
            Transform(circles_group,circles_group.copy().move_to(new_pos))
        ]
        self.play(AnimationGroup(*animations_3,lag_ratio=.5))



        neuron_circle = Circle(radius=1.5, color="GREEN")
        neuron_circle.next_to(circles_group,RIGHT,buff=3)

        animations_4=[
            FadeIn(neuron_circle)
        ]
        self.play(AnimationGroup(*animations_4,lag_ratio=.5))



        lines = VGroup()
        for circle in circles_group:
            line = Line(circle.get_right(),neuron_circle.get_left(),color=WHITE)
            lines.add(line)

        # Add the text
        text = Text("Trainable Weights", color=WHITE,font_size=20)
        text.next_to(lines, UP, buff=.5)

        animations_5=[
            Create(lines,run_time=2),
            FadeIn(text)
        ]
        self.play(AnimationGroup(*animations_5,lag_ratio=.5))


        out_circle = Circle(radius=.5, color="GREEN")
        out_circle.next_to(neuron_circle,RIGHT,buff=1)

        line_o = Line(neuron_circle.get_right(), out_circle.get_left(), color=WHITE)

        animations_6=[
            FadeIn(out_circle),
            Create(line_o, run_time=1),

        ]
        self.play(AnimationGroup(*animations_6,lag_ratio=.5))




        self.wait(2)


    def load_data(self):


        # show first value loaded to input circles
        # show initial weight created and loaaded to lines
        # show initial bias

        # show the formula of aggregation

        # show the aggregation and output
        pass