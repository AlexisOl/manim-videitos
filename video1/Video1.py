
%%manim -qh -v WARNING LimiteEjercicio2


class LimiteEjercicio2(Scene):
    def construct(self):
        # ESCENA 1
        tituloEscena1 = MathTex(r"\lim_{n \longrightarrow \infty} \sqrt{n+1}-\sqrt{n} =0")
        
        # Animación 1
        self.play(Write(tituloEscena1))
        self.wait()
        
        # Mover el título a una esquina
        tituloEscena1_corner = tituloEscena1.copy()
        
        # ESCENA 2
        texto1Escena2 = MathTex(r"\sqrt{\infty+1}-\sqrt{\infty} =\infty")
        texto2Escena2 = Text("Así que por Compresión")
        
        # Como son varios y los quieres manipular como una escena, agrúpalos
        grupoEscena2 = VGroup(texto1Escena2, texto2Escena2).arrange(DOWN).scale(0.8)
        tituloEscena1.generate_target();
        tituloEscena1.target.shift(3*LEFT + 2*UP )
        self.play(
            MoveToTarget(tituloEscena1),  # Animación para mover el título
            Create(grupoEscena2)
        )
        self.wait()

        # ESCENA 3
        texto1Escena3 = MathTex(r"Sean (a_n), (b_n), (c_n), suceciones tal que")
        texto2Escena3 = MathTex(r"(a_n)\leq(b_n)\leq (c_n)")
        texto3Escena3 = MathTex(r"\lim_{n \longrightarrow m}(a_n) = L = \lim_{n \longrightarrow m} (c_n)")
        texto4Escena3 = MathTex(r"\lim_{n \longrightarrow m} (b_n) = L")
        grupoEscena3 = VGroup(texto1Escena3,texto2Escena3,texto3Escena3,texto4Escena3);
        grupoEscena3.arrange(DOWN).scale(0.85);
        ## genera una transformacion

        self.play(
            TransformMatchingShapes(grupoEscena2, grupoEscena3, replace_mobject_with_target_in_scene= True),  
            runtime = 3
        );

        self.wait();
        # ESCENA 4

        #grupo 1
        texto1Escena4 = MathTex(r"\lim_{n \longrightarrow m} (b_n)")
        texto2Escena4 = MathTex(r"\lim_{n \longrightarrow m} (a_n)")
        texto3Escena4 = MathTex(r"\lim_{n \longrightarrow m} (c_n)")
        menorIgual1 = MathTex(r"\leq")
        menorIgual2 = MathTex(r"\leq")
        menorIgual1.next_to(texto2Escena4);
        texto1Escena4.next_to(menorIgual1)
        menorIgual2.next_to(texto1Escena4);
        texto3Escena4.next_to(menorIgual2);
        texto1Escena4.set_color(RED);
        texto2Escena4.set_color(GREEN);
        texto3Escena4.set_color(BLUE);

        grupoEscena4 = VGroup(texto2Escena4,menorIgual1, texto1Escena4, menorIgual2, texto3Escena4)
        grupoEscena4.scale(0.85)

        #grupo 2 

        texto4Escena4 = MathTex(r"0 \leq \lim_{n \to \infty} \frac{(\sqrt{n+1}-\sqrt{n})(\sqrt{n+1}+\sqrt{n})}{\sqrt{n+1}+\sqrt{n}} \leq \lim_{n \to \infty} \frac{1}{\sqrt{n}}")
        grupo2Escena4 = VGroup(grupoEscena4, texto4Escena4)
        grupo2Escena4.arrange(DOWN).scale(0.85)
        self.play(
            TransformMatchingShapes(grupoEscena3,grupo2Escena4, replace_mobject_with_target_in_scene = True ), 
            runtime = 3
        )
        self.wait();

        # ESCENA 5
        texto1Escena5 = MathTex(r"0")
        texto2Escena5 = MathTex(r"\lim_{n \to \infty} \frac{1}{\sqrt{n+1}+\sqrt{n}}")
        texto3Escena5 = MathTex(r"\lim_{n \to \infty} \frac{1}{\sqrt{n}}")
        menorIgual1_escena5 = MathTex(r"\leq")
        menorIgual2_escena5 = MathTex(r"\leq")
        texto1Escena5.set_color(GREEN);
        texto2Escena5.set_color(RED);
        texto3Escena5.set_color(BLUE);
        menorIgual1_escena5.next_to(texto1Escena5);
        texto2Escena5.next_to(menorIgual1_escena5)
        menorIgual2_escena5.next_to(texto2Escena5);
        texto3Escena5.next_to(menorIgual2_escena5);
        grupoEscena5 = VGroup(texto1Escena5,menorIgual1_escena5, texto2Escena5, menorIgual2_escena5, texto3Escena5);
        grupoEscena5.scale(0.85)
        grupo2Escena5 =VGroup(grupoEscena4, grupoEscena5)
        grupo2Escena5.arrange(DOWN)

        self.play(
            TransformMatchingShapes(grupo2Escena4,grupo2Escena5, replace_mobject_with_target_in_scene = True ), 
            runtime = 3
        )
        self.wait();

        # ESCENA 6

        texto1Escena6 = MathTex(r"\lim_{n \to \infty} \frac{1}{\sqrt{n}} =0")
        texto2Escena6 = Text('al usar compresion tenemos que')
        texto3Escena6 = MathTex(r"\lim_{n \longrightarrow \infty} \sqrt{n+1}-\sqrt{n} =0 \blacksquare")
        grupoEscena6 = VGroup(texto1Escena6, texto2Escena6 , texto3Escena6)
        grupoEscena6.arrange(DOWN).scale(0.85)

        self.play(
            TransformMatchingShapes(grupo2Escena5,grupoEscena6, replace_mobject_with_target_in_scene = True ), 
            runtime = 3
         )
        self.wait();
        # ESCENA 7
   
        self.play(
            tituloEscena1.animate.scale(0.80).move_to(2*DOWN +2.2*RIGHT),  # Animación para mover el título
            Uncreate(grupoEscena6)
        )
        self.wait()

        #agrego plano

        self.wait()
        self.grafica();

    
    ##### metodo para funcion

    def grafica(self):
      ejes = Axes(
          y_range=[0,5,1],
          x_range=[0, 12, 1],
          x_length=10
      )
      ejes.add_coordinates();

      self.play(
          Write(ejes)
          
      )
      self.wait();
      funcion= ejes.plot(lambda x: (x+1)**(1/2)- (x)**(1/2),
                         color= RED)

      self.play(
          FadeIn(funcion)
          
      )
      self.wait(2);

