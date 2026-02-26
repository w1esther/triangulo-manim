from manim import *
import numpy as np

class AreaTriangulo(MovingCameraScene):
    def construct(self):

        base1 = MathTex("b_{base}")
        # base2 = MathTex("b_{base}")

        base1.shift(2.4*DOWN, 1*RIGHT)
        base1.scale(0.8)
        # base2.shift(2*DOWN, 1*RIGHT)

        altura1 = MathTex("h_{altura}")
        # altura2 = MathTex("h_{altura}")

        altura1.shift(0.8*RIGHT)
        altura1.scale(0.8)
        # altura2.shift(2*RIGHT)

        A = np.array([-1, -2,0])
        B = np.array([3, -2,0])
        C = np.array([0, 2,0])

        grupo_tri1 = VGroup()
        grupo_tri2 = VGroup()

        tri_1 = Polygon(A, B, C, color=BLUE_B)
        tri_2 = Polygon(A, B, C, color=RED)

        altura_tr1 = Line(C, 2*DOWN)
        altura_tr2 = Line(C, 2*DOWN)

        linha_base1 = Line(A, B, color=YELLOW)
        linha_base2 = Line(A, B, color=YELLOW)

        grupo_tri1.add(altura_tr1, tri_1, altura1, base1, linha_base1)

        grupo_tri2.add(altura_tr2, tri_2, linha_base2)

        self.play(Write(grupo_tri1), Write(grupo_tri2), run_time=4)

        self.wait(2)

        self.play(grupo_tri1.animate.shift(2*LEFT), grupo_tri2.animate.shift(2*LEFT))

        self.wait(2)

        self.play(grupo_tri2.animate.shift(3*RIGHT))

        self.wait(2)

        self.play(grupo_tri2.animate.rotate(180*DEGREES))

        self.wait(2)

        self.play(grupo_tri2.animate.shift(2*LEFT))

        self.wait(2)

        self.play(grupo_tri1.animate.set_fill(GREEN, opacity=0.3), grupo_tri2.animate.set_fill(GREEN, opacity=0.3))

        self.wait(2)

        label_paralelogramo = MathTex('Paralelogramo')

        label_paralelogramo.shift(2.5*UP)

        self.play(FadeIn(label_paralelogramo))

        self.wait(2)

        self.play(self.camera.frame.animate.shift(2*RIGHT))

        self.wait(2)

        label_area_paralelogramo = MathTex('Area do Paralelogramo:')

        label_area_paralelogramo.shift(1.5*UP + 5.5*RIGHT)

        area_paralelogramo = MathTex('b_{base} \cdot h_{altura}')

        area_paralelogramo.shift(0.7*UP + 5.2*RIGHT)

        self.play(Create(area_paralelogramo), Create(label_area_paralelogramo))

        self.wait(2)

        label_area_triangulo = MathTex('Area do Triangulo:')

        label_area_triangulo.shift(5.2*RIGHT, 0.6*DOWN)

        area_triangulo1 = MathTex(r'\frac{area do paralelogramo}{2}')

        area_triangulo1.scale(0.7).shift(1.6*DOWN, 5.2*RIGHT)

        self.play(Create(label_area_triangulo), Create(area_triangulo1))

        self.wait(2)

        area_triangulo2 = MathTex(r'\frac{b_{base} \cdot h_{altura}}{2}')

        area_triangulo2.scale(0.7).shift(1.6*DOWN, 5.2*RIGHT)

        self.play(Transform(area_triangulo1, area_triangulo2))

        self.wait(2)