import numpy as np
from manim import *
from numpy import array
import random

class ShowAnimation(Scene):

    def construct(self):

        self.train_inputs = array([[0, 0, 0], [1, 1, 1], [1, 0, 1], [0, 1, 1], [0, 1, 0]])
        self.output = array([[0], [1], [1], [0], [0]])

        self.weight_matrix = self.weights()

        #show input / output
        #self.data_scene(self.train_inputs,self.output)

        self.clear()

        self.create_network(self.train_inputs , self.output,self.weight_matrix)
        self.clear()


    def data_scene(self,train_inputs,output):


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


    def create_network(self,train_inputs, output,weight_matrix):

        inp_1_circle = Circle(radius=.5, color="BLUE")
        inp_2_circle = Circle(radius=.5, color="BLUE")
        inp_3_circle = Circle(radius=.5, color="BLUE")

        circles_group = VGroup(inp_1_circle, inp_2_circle, inp_3_circle).arrange(DOWN, buff=0.5)

        inp_1_circle.move_to([-4,1.5,0])
        inp_2_circle.next_to(inp_1_circle,DOWN)
        inp_3_circle.next_to(inp_2_circle, DOWN)

        text = Text("Input \nLayer", color=WHITE,font_size=20)
        text.next_to(inp_1_circle, UP, buff=1)

        animations_3=[
            Create(circles_group),
            FadeIn(text)
        ]
        self.play(AnimationGroup(*animations_3,lag_ratio=.5))



        neuron_circle = Circle(radius=1.5, color="GREEN")
        neuron_circle.next_to(circles_group,RIGHT,buff=3)
        text = Text("Neuron", color=WHITE,font_size=20)
        text.next_to(neuron_circle, UP, buff=1)

        animations_4=[
            FadeIn(neuron_circle),
            FadeIn(text)
        ]
        self.play(AnimationGroup(*animations_4,lag_ratio=.5))



        lines = VGroup()
        for circle in circles_group:
            line = Line(circle.get_right(),neuron_circle.get_left(),color=WHITE)
            lines.add(line)

        # Add the text
        text = Text("Trainable \n Weights", color=WHITE,font_size=20)
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


        inp_matrix=Matrix(train_inputs,
            v_buff=0.5,
            h_buff=0.5,
            bracket_h_buff=SMALL_BUFF,
            bracket_v_buff=SMALL_BUFF
            )
        inp_matrix.next_to(inp_2_circle,LEFT)

        animations_7=[
            FadeIn(inp_matrix)
        ]
        self.play(AnimationGroup(*animations_7,lag_ratio=.5))

        first_row_highlight = SurroundingRectangle(inp_matrix.get_rows()[1], color="green")

        # Create and position elements inside the circles
        f_element = Tex('x1 = '+str(train_inputs[1][0]), font_size=30).move_to(inp_1_circle)
        s_element = Tex('x2 = '+str(train_inputs[1][1]), font_size=30).move_to(inp_2_circle)
        t_element = Tex('x3 = '+str(train_inputs[1][2]), font_size=30).move_to(inp_3_circle)

        # Create animation sequence
        animations = [
            Create(first_row_highlight),
            FadeIn(f_element),
            FadeIn(s_element),
            FadeIn(t_element)
        ]

        self.play(*animations, lag_ratio=0.5)
        weights_txt = Text("Initial Weights",font_size=20)

        matrix_scale = 0.6


        wt_matrix=Matrix(weight_matrix,
            v_buff=0.5,
            h_buff=0.5,
            bracket_h_buff=SMALL_BUFF,
            bracket_v_buff=SMALL_BUFF
            )
        wt_matrix.scale(matrix_scale)
        wt_matrix.set_font_size(.3)

        wt_matrix.next_to(lines,DOWN, buff=1)
        weights_txt.next_to(wt_matrix,LEFT)

        i=1
        array_elements =[]
        for element in weight_matrix:
            array_elements.append(Text('w'+str(i)+' = '+str(element), font_size=20))
            i+=1
        array_elements[0].next_to(lines[0],UP,buff=0)
        array_elements[1].next_to(lines[1],UP,buff=0)
        array_elements[2].next_to(lines[2],DOWN,buff=0)


        self.play(
            FadeIn(weights_txt),
            FadeIn(wt_matrix),
            *[FadeIn(element) for element in array_elements]
        )

        line = Line(neuron_circle.get_top(), neuron_circle.get_bottom(), color=WHITE)
        vertical_line = DashedLine(neuron_circle.get_top(), neuron_circle.get_bottom(), color=WHITE)

        self.play(Create(vertical_line))

        agg_label =Text("Weighted \n Sum", font_size=15 ,color=RED)
        agg_label.next_to(neuron_circle.get_left(),UP, buff = 2)

        act_function_txt =Text("Activation \n Function", font_size=15 , color=YELLOW)
        act_function_txt.next_to(neuron_circle.get_right(),UP, buff = 2)


        aggregate = MathTex(r"\sum_{i=1}^{n} x_i w_i",color=RED)
        aggregate.next_to(neuron_circle.get_left(),RIGHT, buff=.05)
        aggregate.set_font_size(30)

        sigmoid_text = MathTex(r"\sigma(x) =\frac{1}{1 + e^{-x}}",color=YELLOW)
        sigmoid_text.next_to(neuron_circle.get_right(), LEFT, buff=-1)
        sigmoid_text.set_font_size(20)

        z = train_inputs[1][0]*weight_matrix[0] +train_inputs[1][1]*weight_matrix[1]+train_inputs[1][2]*weight_matrix[2]

        z = Text(str(z) , color=RED)
        z.next_to(neuron_circle.get_left(),DOWN, buff=1.5)
        z.set_font_size(15)

        self.play(FadeIn(aggregate),FadeIn(sigmoid_text),FadeIn(agg_label),FadeIn(act_function_txt),FadeIn(z))

        self.wait(2)

    def load_data(self,train_inputs, output,weight_matrix):

        # show first value loaded to input circles
        # show initial weight created and loaaded to lines
        # show initial bias

        # show the formula of aggregation

        # show the aggregation and output


        pass


    def weights(self):

        random.seed(1)
        weight_arr = np.random.rand(3,1)

        self.weight_matrix = (2*weight_arr)-1

        return self.weight_matrix

    def sig(self,x):

        return np.sig(x)

    def tanh_derivative(self,x):

        return 1- np.tanh(x) **2

