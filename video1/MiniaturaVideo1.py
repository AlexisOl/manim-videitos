%%manim -qh -v WARNING GradientImageFromArray
class GradientImageFromArray(Scene):
    def construct(self):
        texto = Text('Determine el valor de')
        MateTexto = MathTex(r'\lim_{n \longrightarrow \infty} \sqrt{n+1}-\sqrt{n} =0')
        titulo = VGroup(texto, MateTexto).arrange(DOWN)
        framebox1 = SurroundingRectangle(titulo, buff = .5,fill_color=BLUE, fill_opacity=0.2)

        self.add(
            
            titulo, framebox1

            )