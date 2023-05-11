from manim import *
from numpy import array
import random

class ShowAnimation(Scene):

    def construct(self):


        #show input / output
        #self.data_scene()
        #self.clear()

        self.create_network()
        self.clear()

    def data_scene(self):
        inp_txt =Text("Input",font_size=20)
        train_inputs = array([[0,0,0],[1,1,1],[1,0,1],[0,1,1],[0,1,0]])
        out_txt = Text("Expected \n Output",font_size=20)
        output = array([[0],[1],[1],[0],[0]])

        inp_matrix=Matrix(train_inputs,
            v_buff=0.6,
            h_buff=0.6,
            bracket_h_buff=SMALL_BUFF,
            bracket_v_buff=SMALL_BUFF
            )

        out_matrix=Matrix(output,
            v_buff=0.6,
            h_buff=0.6,
            bracket_h_buff=SMALL_BUFF,
            bracket_v_buff=SMALL_BUFF
            )

        inp_txt.move_to([-5,3,0])

        inp_matrix.next_to(inp_txt,DOWN)
        out_txt.next_to(inp_txt,RIGHT).shift(.5*RIGHT)
        out_matrix.next_to(inp_matrix)


        fir_1 = SurroundingRectangle(inp_matrix.get_rows()[0],color="Green",buff=.1)
        fir_2 = SurroundingRectangle(inp_matrix.get_rows()[1],color="Green",buff=.1)
        fir_3 = SurroundingRectangle(inp_matrix.get_rows()[2],color="Green",buff=.1)
        fir_4 = SurroundingRectangle(inp_matrix.get_rows()[3],color="Green",buff=.1)
        fir_5 = SurroundingRectangle(inp_matrix.get_rows()[4],color="Green",buff=.1)

        for_1 = SurroundingRectangle(out_matrix.get_rows()[0],color="Yellow",buff=.1)
        for_2 = SurroundingRectangle(out_matrix.get_rows()[1],color="Yellow",buff=.1)
        for_3 = SurroundingRectangle(out_matrix.get_rows()[2],color="Yellow",buff=.1)
        for_4 = SurroundingRectangle(out_matrix.get_rows()[3],color="Yellow",buff=.1)
        for_5 = SurroundingRectangle(out_matrix.get_rows()[4],color="Yellow",buff=.1)


        animations = [
            FadeIn(inp_txt),
            Create(inp_matrix),
            FadeIn(out_txt),
            Create(out_matrix)
        ]
        self.play(AnimationGroup(*animations,lag_ratio=.5))
        self.wait(.5)

        animations_1 = [
            Create(fir_1),
            Create(for_1)
        ]
        self.play(AnimationGroup(*animations_1,lag_ratio=.5))
        animations_2 = [
            ReplacementTransform(fir_1, fir_2),
            ReplacementTransform(for_1, for_2),
        ]
        self.play(AnimationGroup(*animations_2))
        animations_3 = [
            ReplacementTransform(fir_2, fir_3),
            ReplacementTransform(for_2, for_3)
        ]
        self.play(AnimationGroup(*animations_3))
        animations_4 = [
            ReplacementTransform(fir_3, fir_4),
            ReplacementTransform(for_3, for_4)
        ]
        self.play(AnimationGroup(*animations_4))
        animations_5 = [
            ReplacementTransform(fir_4, fir_5),
            ReplacementTransform(for_4, for_5)
        ]
        self.play(AnimationGroup(*animations_5))
        self.wait()

    def create_network(self):

        inp_1_circle = Circle(radius=.5, color="BLUE")
        inp_2_circle = Circle(radius=.5, color="BLUE")
        inp_3_circle = Circle(radius=.5, color="BLUE")

        inp_1_circle.move_to([-5,3,0])
        inp_2_circle.next_to(inp_1_circle,DOWN)
        inp_3_circle.next_to(inp_2_circle, DOWN)

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
            Create(inp_1_circle),
            Create(inp_2_circle),
            Create(inp_3_circle),
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

        self.wait(2)w
