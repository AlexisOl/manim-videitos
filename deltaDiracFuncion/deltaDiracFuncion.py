#comnado ejecucion
%%manim -ql -v WARNING LimiteEjercicio2

##config dimensiones

class LimiteEjercicio2(Scene):
  
    def construct(self):

      self.graficaLimiteDirac();
      self.wait()


    ##### metodo para funcion

    def graficaLimiteDirac(self):
      ejes= Axes (
           y_range=[0,4,1],
          x_range=[-10, 10, 2]
      )
      ejes.add_coordinates();

      self.play(Write(ejes));
      self.wait();
      self.graficaDirac(ejes)


    def graficaDirac(self, ejes):

      self.wait();
      #grupo de funciones

      funciones = VGroup();
      textoDirac = MathTex(r'f(x) = \frac{n}{\sqrt{\pi}}e^{-{n^{-2}x^2}}').scale(0.8)
      textoDirac.shift(2*UP + 2.5*LEFT)

      self.play(Write(textoDirac))
      self.wait()

      for i in np.arange(0.1, 5, 0.2):
        texto = Text(f"a = {i}");
        self.wait(1);
        funcion=ejes.plot(lambda x: np.exp(-(x**2)/((i)**2))/((np.pi)*(i)**2)**(1/2),
                         color= RED)
        funciones+= ejes.plot(lambda x: np.exp(-(x**2)/((i)**2))/((np.pi)*(i)**2)**(1/2),
                         color= YELLOW)

        self.play(
            texto.animate.scale(0.60).move_to(2*UP + 3*RIGHT),

            FadeIn(funcion),

              run_time=0.2

            )
        self.wait()
        self.play(
            Unwrite(texto)

        )

      textoDirac2 = MathTex(r'\lim_{n \longrightarrow 0} f(x) = \delta(x) ')
      textoDirac2.shift(2*UP + 2.5*LEFT)
      self.play(TransformMatchingShapes(textoDirac,textoDirac2, replace_mobject_with_target_in_scene = True), runtime = 3,
               )
      self.wait()


      self.play(
          FadeIn(funciones)

      )
      self.wait(2);

