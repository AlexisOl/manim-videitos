### VIDEO FINAL DE LO QUE HABALARE

%%manim -ql videoTaller


##algunas importaciones de video
import cv2
from PIL import Image, ImageOps
from dataclasses import dataclass
@dataclass
## uso la libreria de cv2 para la captura de videos
## clase para ver videos
##################################
##################################
##################################
##################################

class VideoStatus:
    time: float = 0
    videoObject: cv2.VideoCapture = None
    def __deepcopy__(self, memo):
        return self

class VideoMobject(ImageMobject):
    def __init__(self, filename=None, imageops=None, speed=1.0, loop=False, **kwargs):
        self.filename = filename
        self.imageops = imageops
        self.speed = speed
        self.loop = loop
        self.status = VideoStatus()
        self.status.videoObject = cv2.VideoCapture(filename)
        self.status.videoObject.set(cv2.CAP_PROP_POS_FRAMES, 1)
        ret, frame = self.status.videoObject.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            if imageops:
                img = imageops(img)
        else:
            img = Image.fromarray(np.uint8([[63, 0, 0], [0, 127, 0], [0, 0, 191]]))
        super().__init__(img, **kwargs)
        if ret:
            self.add_updater(self.videoUpdater)

    def videoUpdater(self, mobj, dt):
        status = self.status
        status.time += 1000 * dt * mobj.speed
        status.videoObject.set(cv2.CAP_PROP_POS_MSEC, status.time)
        ret, frame = status.videoObject.read()
        if (not ret) and self.loop:
            status.time = 0
            status.videoObject.set(cv2.CAP_PROP_POS_MSEC, status.time)
            ret, frame = status.videoObject.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            if mobj.imageops:
                img = mobj.imageops(img)
            mobj.pixel_array = change_to_rgba_array(np.asarray(img), mobj.pixel_array_dtype)


##################################
##################################
##################################
##################################
##################################
## transiciones
def TransitionTo(scene_class):
     return scene_class()

##################################
##################################
##################################
##################################
##################################
## clase general
class videoTaller(Scene):
    def construct(self):
      self.generacionPrincipalManim()
      self.wait(1)
      self.grupoTeorico()
      self.wait(1)
      self.grupoDiedrico()
      self.wait(1)
      #self.play(FadeOut(self.mobjects))  
      self.videoPermutacionesZ12()
      #self.permutacionesZ7();
      self.wait(1)
      self.casosReales()
      self.wait(1)
      self.aplicacionMusical()
      self.wait(1)
      self.Tonnetz()
      self.wait(1)
     # self.play(TransitionTo(toroTonnetz))
      self.videoToro()

##################################
##################################
##################################
##################################
## 1. sobre manim
    def generacionPrincipalManim(self):
      ## que vaya como que a un lado
      textoInicial = Text("¿Que es Manim?")
      self.play(Write(textoInicial, run_time = 3))

      textoInicial2 = Text("Esta es una libreria de Python para realizar animaciones")
      textoInicial3 = Text("Esta fue hecha por Grant Sanderson")

      ## generar un v group agrupando los elementos de texto y de imagen
      ##generacion de un vgroup
      grupoTexto = VGroup(textoInicial, textoInicial2, textoInicial3).arrange(DOWN).scale(0.45)
      imagen = ImageMobject("/content/grant-1.png").move_to(RIGHT*4.3).scale(0.50)

      self.play(Transform(textoInicial,grupoTexto ))
      self.wait(2)
  ## mover el grupo a la izquierda
      self.play((grupoTexto.animate.shift(LEFT*2.5)), run_time = 3)
      self.wait(2)
      ## agrega la imagen
      self.add(imagen)
      self.wait(3)

      self.play(Unwrite(grupoTexto))
      self.remove(imagen)
      self.generacionVideos()
      self.wait(1)




      ## llamo a otros videos y uso de imageMobject

        ### metodo para los videos
    def generacionVideos(self):
          ## losta de videos
              video1 = VideoMobject(
                  filename=r"/content/videos/video3d.mp4",
                  speed=2.0
              ).scale_to_fit_width(5).to_corner(UL)
              video2 = VideoMobject(
                  filename=r"/content/videos/funcionesCambiantes.mp4",
                  speed=2.0,
                  loop=True,
              ).scale_to_fit_width(5).to_corner(UR)
              video3 = VideoMobject(
                  filename=r"/content/videos/koch.mp4",
                  speed=2.0,
                  loop=True,
              ).scale_to_fit_width(5).to_corner(DR)
              video4 = VideoMobject(
                  filename=r"/content/videos/fractalArbol.mp4",
                  speed=2.0,
                  loop=True,
              ).scale_to_fit_width(5).to_corner(DL)
              v1 = Group(video1, SurroundingRectangle(video1))
              v2 = Group(video2, SurroundingRectangle(video2))
              v3 = Group(video3, SurroundingRectangle(video3))
              v4 = Group(video4, SurroundingRectangle(video4))
              self.add(v1,v2, v3, v4)
              self.wait(10)
      ### visualizacion rapida de uno de ellos y fragmento de codigo
              self.remove(v1,v2,v4)
              self.play((v3.animate.shift(LEFT*8+UP*3).scale(1.2)), run_time = 5)
              codigoUsado = '''
              %%manim -ql KochCurve
              class KochCurve(Scene):
                  def construct(self):

                      ## una recta en x
                      l = Line([-5, 0, 0], [5, 0, 0], color = WHITE)

              ## se agrega
                      self.add(l)
                      self.wait()

              ## creacmos un grupo vectorial
                      gPrev = VGroup(l)
                      gNow = VGroup()

              ## iteraciones
                      maxIter = 10

                      for i in range(maxIter):
                        ## nuevos vgrupos
                          gNow = VGroup()
                          ## ciclo para cada valor en el primer grupo vectorial
                          for l in gPrev:
                            ## obtiene la cantidad de valor de inicio y fin
                              direction =  l.get_start() - l.get_end()
                              ## como coch tiene una horientacion de 45 caso
                              ## generacion de lineas
                              l1  = l.copy().scale(1/3).shift(direction/3)
                              l2 = l.copy().scale(1/3).shift(-direction/3)

                              ## copia de linea inclinadas
                              l3 = l.copy().scale(1/3)
                              ## generacion de punto
                              pt = l3.get_start()
                              ### rotacion de pi/4
                              l3.rotate(PI/3, about_point = pt)
                              l4 = l.copy().scale(1/3)

                              pt = l4.get_end()
                              l4.rotate(-PI/3, about_point = pt)
                              #### agrega los valors en el grupo
                              gNow.add(l1, l3, l4, l2)

                          self.clear()
                          ## imprime
                          self.play(Write(gNow))
                          self.wait()
                          ## vuelve a iterar
                          gPrev = gNow
              '''
              rendered_code = Code(code=codigoUsado, tab_width=4, background="window",
                                  language="Python", font="Monospace")
              codigoGrupo = Group(rendered_code, SurroundingRectangle(rendered_code)).scale(0.4).shift(RIGHT * 4)
              self.add(codigoGrupo)
              self.wait(5)
              self.play(FadeOut(codigoGrupo, v3), )




#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
## 2. definicion de lo que es un grupo


### 2.1 definicion de lo que es un grupo
    def grupoTeorico(self):
      texto1 = MathTex(r"Grupos")
      texto2 = MathTex(r"\text{Un grupo es una estructura algebraica}")
      texto3 = MathTex(r"\text{dada por una operacion binaria}")
      definicionFormal = MathTex(r"\text{Un grupo es un conjunto no vacío } G, \text{ junto con una operación binaria } *: G \times G \longrightarrow G")
      condicion1 = MathTex(r"\text{Debe ser asociativo: } a, b, c \in G, \, a * (b * c) = (a * b) * c")
      condicion2 = MathTex(r"\text{Debe tener elemento neutro } e \in G: \, a * e = a = e * a")
      condicion3 = MathTex(r"\text{Debe tener elemento inverso: para cada } a \in G, \text{ existe } a' \in G \text{ tal que } a * a' = e = a' * a")

      self.play(Write(texto1, run_time = 3))
      grupoTexto = VGroup(texto1, texto2, texto3).arrange(DOWN).scale(0.60)
      self.play(Transform(texto1, grupoTexto, run_time = 3))
      self.wait(4)
      grupoTextoFormal = VGroup(definicionFormal, condicion1, condicion2, condicion3).arrange(DOWN).scale(0.60)

      self.play(Transform(grupoTexto,grupoTextoFormal ))
      self.wait(10)
      self.remove(grupoTextoFormal, grupoTexto)
      self.wait(2)

## 2. 2 vista de grupos diedrico
    def grupoDiedrico(self):
        # Crear un pentágono regular
        pentagono = RegularPolygon(n=5, color=WHITE)
        vertices = pentagono.get_vertices()
        labels = VGroup()

        # Añadir etiquetas en cada vértice para visualizar los cambios
        for i, vertice in enumerate(vertices):
            label = Text(str(i + 1), font_size=24, color=YELLOW).move_to(vertice * 1.1)
            labels.add(label)

        # Agrupar pentágono y etiquetas
        grupo_pentagono = VGroup(pentagono, labels)

        # Posiciona el grupo en el centro
        self.add(grupo_pentagono)

        # Aplicar rotaciones (5 rotaciones en total para D5)
        angulo_rotacion = 2 * PI / 5
        for i in range(5):
            self.play(Rotate(grupo_pentagono, angle=angulo_rotacion), run_time=1)
            self.wait(0.5)

        # Espera final
        self.wait(2)
        self.play(Uncreate(grupo_pentagono))
        self.wait(1)

  ## 2.3 idea  de un grupo a traves de una grafica de Cayley y sus permutaciones
    def videoPermutacionesZ12(self):
          ## losta de videos
              videoZ12 = VideoMobject(
                  filename=r"/content/videos/D12Rotations.mp4",
                  speed=0.5
              ).scale_to_fit_width(5).to_corner(UL)
            
              v1 = Group(videoZ12, SurroundingRectangle(videoZ12))
   
              self.wait(10)
      ### visualizacion rapida de uno de ellos y fragmento de codigo
              self.play((v1.animate.shift(RIGHT*3+DOWN*3).scale(2)), run_time = 5)
              self.remove(v1)

### 2.4 tabla de cayley del z7
    def tablaCayleyZ7(self):
        elements = list(range(7))
        table_data = [["+"] + elements]

        for i in elements:
            row = [i] + [(i + j) % 7 for j in elements]
            table_data.append(row)

        # Crear la tabla con Manim
        table = Table(
            table_data,
            col_labels=[MathTex(str(e)) for e in ["+"] + elements],
            row_labels=[MathTex(str(e)) for e in elements],
            h_buff=0.8, v_buff=0.8
        )

        table.scale(0.7)  # Escalar para que se ajuste a la pantalla
        table.get_cell((1, 1), color=BLUE)  # Color de la celda superior izquierda
        table.get_horizontal_lines().set_color(BLUE)
        table.get_vertical_lines().set_color(BLUE)

        # Mostrar la tabla en la escena
        self.play(Create(table))
        self.wait(3)


#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################

### 3. visualizacion de estos en la vida real
    def casosReales(self):
   # Textos iniciales
        texto1 = Text("Se puede visualizar esta idea en distintos aspectos de la vida real").scale(0.50)
        texto2 = Text("Como biología, química, económica, física, entre otras").scale(0.50)
        texto3 = Text("No obstante, su aplicación se puede apreciar en la naturaleza").scale(0.50)

        # Imágenes
        imagen1 = ImageMobject("/content/img/img1.png").scale(0.50)
        imagen2 = ImageMobject("/content/img/img2.png").scale(0.50)
        imagen3 = ImageMobject("/content/img/img3.png").scale(0.50)
        imagen4 = ImageMobject("/content/img/img4.jpg").scale(0.50)
        imagen5 = ImageMobject("/content/img/img5.jpg").scale(0.50)

        # Agrupar textos
        grupoTexto = Group(texto1, texto2, texto3).arrange(DOWN)
        self.play(FadeIn(grupoTexto))
        self.wait(5)
        self.play(FadeOut(grupoTexto))
        # Posicionar las imágenes una al lado de la otra
        imagen2.next_to(imagen1, RIGHT, buff=0.5)
        imagen3.next_to(imagen2, RIGHT, buff=0.5)
        imagen4.next_to(imagen1, LEFT, buff=0.5)
        imagen5.next_to(imagen4, LEFT, buff=0.5)

        # Agrupar imágenes
        grupoImagenes = Group(imagen1, imagen2, imagen3, imagen4,imagen5)
        self.add(grupoImagenes)
        self.wait(5)

        # Usar remove para eliminar los grupos
        self.remove(grupoTexto, grupoImagenes)
        self.wait(1)  # Esperar un momento para ver el resultado





#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################

### 4 aplicacion en la musica
    def aplicacionMusical(self):
        textoIntroductorio = Text("Ahora analizaremos esta teoría con la música").scale(0.6)
        texto1 = Text("El rango de tonos que comienza con una frecuencia hasta su doble, se conoce como una octava.").scale(0.6)
        texto2 = Text("Esta se divide en 12 intervalos").scale(0.6)
        texto3 = Text("El conjunto completo de doce notas se llama la escala cromática").scale(0.6)
        
        self.play(Create(textoIntroductorio), runtime=3)
        self.wait(5)

        grupoTexto = VGroup(texto1, texto2, texto3).arrange(DOWN).scale(0.6)
        self.play(Uncreate(textoIntroductorio), Create(grupoTexto), runtime=3)
        self.wait(5)

        texto4 = Text("Tenemos a la escala cromática como").scale(0.6)
        texto5 = Text("C, C#, D, D#, E, F, F#, G, G#, A, A#, B.").scale(0.6)
        texto6 = Text("Analizaremos un conjunto especial de notas, las triadas").scale(0.6)
        texto7 = Text("donde tenemos").scale(0.6)

        grupoTexto2 = VGroup(texto4, texto5, texto6, texto7).arrange(DOWN).scale(0.6)
        self.play(Uncreate(grupoTexto), Create(grupoTexto2), runtime=3)
        self.wait(5)

        text8 = Text("Acordes Menor").scale(0.9)
        text9 = MathTex(r"a, b, c \in \mathcal{Z}_{12} | b = a + 3; c = a + 7").scale(0.9)
        text10 = Text("Acordes Mayor").scale(0.9)
        text11 = MathTex(r"a, b, c \in \mathcal{Z}_{12} | b = a + 4; c = a + 7").scale(0.9)

        text8.set_color(RED)
        text10.set_color(GREEN)

        grupoTextoMayor = VGroup(text8, text9).arrange(DOWN)
        grupoTextoMenor = VGroup(text10, text11).arrange(DOWN)
        grupoAcordes = VGroup(grupoTextoMayor, grupoTextoMenor).arrange(RIGHT).scale(0.6)

        self.play(Uncreate(grupoTexto), Uncreate(grupoTexto2), Create(grupoAcordes), runtime=3)
        self.wait(5)

        text12 = Text("Donde podemos encontrar una serie de clases residuales en base al grupo").scale(0.6)
        text13 = MathTex(r"\mathcal{Z}_{12} = [0],[1], ... [11]").scale(0.5)
        clasesResiduales = VGroup()

        for i in range(12):
            sequence_text = MathTex(
                rf"[{i}] = \{{ ... {-24 +  i}, {-12 + i}, {i}, {12 +  i},{ 24 + i}, ... \}}"
            ).scale(0.6)  # Escala para cada secuencia
            sequence_text.next_to(UP * (5 - i))  # Ajusta el valor 5 según el espacio necesario
            clasesResiduales.add(sequence_text)

        clasesResiduales.shift(UP*0.5+LEFT*3)
        self.play(Uncreate(grupoAcordes), Create(clasesResiduales.scale(0.7)), runtime=3)
        self.wait(5)

        text16 = Text("Transformaciones determinadas").scale(0.6)
        text17 = Text("Transposición").scale(0.6)
        text18 = Text("Inversión").scale(0.6)

        grupoTexto3 = VGroup(text16, text17, text18).arrange(DOWN).scale(0.6)
        self.play(Uncreate(clasesResiduales), Create(grupoTexto3), runtime=3)
        self.wait(5)
        self.play(Uncreate(grupoTexto3))
    # Definir los vértices y bordes para el primer grafo
        vertices_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        edges_1 = [
              (0, 4), (4, 7), (7, 0),
              (0, 1), (1, 2), (2, 3),
              (3, 4), (4, 5), (5, 6),
              (6, 7), (7, 8), (8, 9),
              (9, 10), (10, 11), (11, 0)
          ]
          
          # Crear el primer grafo con un tamaño más pequeño
        g1 = Graph(
              vertices_1,
              edges_1,
              layout="circular",
              layout_scale=2,  # Reducir el tamaño del grafo
              labels=True,
              vertex_config={
                  0: {"fill_color": RED},
                  7: {"fill_color": RED},
                  4: {"fill_color": RED}
              },
              edge_config={
                  (0, 4): {"stroke_color": RED},
                  (7, 0): {"stroke_color": RED},
                  (4, 7): {"stroke_color": RED}
              }
          )

          # Definir los vértices y bordes para el segundo grafo
        vertices_2 =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        edges_2 = [            
              (0, 1), (1, 2), (2, 3),
              (3, 4), (4, 5), (5, 6),
              (6, 7), (7, 8), (8, 9),
              (9, 10), (10, 11), (11, 0),
              (1, 5), (5, 8), (8, 1)  # Ejemplo de bordes
          ]  
          
          # Crear el segundo grafo con un tamaño más pequeño
        g2 = Graph(
              vertices_2,
              edges_2,
              layout="circular",
              layout_scale=2,  # Reducir el tamaño del grafo
              labels=True,
              vertex_config={
                  1: {"fill_color": BLUE},
                  5: {"fill_color": BLUE},
                  8: {"fill_color": BLUE}
              },
              edge_config={
                  (1, 5): {"stroke_color": BLUE},
                  (5, 8): {"stroke_color": BLUE},
                  (8, 1): {"stroke_color": BLUE}
              }
          )

                  # Definir los vértices y bordes para el segundo grafo
        vertices_3 =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        edges_3 = [            
              (0, 1), (1, 2), (2, 3),
              (3, 4), (4, 5), (5, 6),
              (6, 7), (7, 8), (8, 9),
              (9, 10), (10, 11), (11, 0),
              (2, 6), (6, 9), (9, 2)  # Ejemplo de bordes
          ]  
          
          # Crear el segundo grafo con un tamaño más pequeño
        g3 = Graph(
              vertices_3,
              edges_3,
              layout="circular",
              layout_scale=2,  # Reducir el tamaño del grafo
              labels=True,
              vertex_config={
                  2: {"fill_color": GREEN},
                  6: {"fill_color": GREEN},
                  9: {"fill_color": GREEN}
              },
              edge_config={
                  (2, 6): {"stroke_color": GREEN},
                  (6, 9): {"stroke_color": GREEN},
                  (9, 2): {"stroke_color": GREEN}
              }
          )

        title2 = Text("Transposiciones de C").next_to(g2, UP)
          # Ajustar la posición del segundo grafo para que no se superponga
        g1.move_to(LEFT * 5)  # Mueve el segundo grafo a la derecha para que estén a la par
          
        g2.next_to(g1, RIGHT)  # Mueve el segundo grafo a la derecha para que estén a la par
        g3.next_to(g2, RIGHT)  # Mueve el segundo grafo a la derecha para que estén a la par

          # Añadir ambos grafos a la escena
        self.play(Create(title2), Create(g1), Create(g2), Create(g3))

        self.wait(6)
        self.play(Uncreate(title2), Uncreate(g1), Uncreate(g2), Uncreate(g3))



          # Definir los vértices y bordes para el primer grafo
        vertices_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        edges_1 = [
              (2, 6), (6, 11), (11, 2),
              (0, 1), (1, 2), (2, 3),
              (3, 4), (4, 5), (5, 6),
              (6, 7), (7, 8), (8, 9),
              (9, 10), (10, 11), (11, 0)
          ]
          
          # Crear el primer grafo con un tamaño más pequeño
        g1 = Graph(
              vertices_1,
              edges_1,
              layout="circular",
              layout_scale=2,  # Reducir el tamaño del grafo
              labels=True,
              vertex_config={
                  2: {"fill_color": RED},
                  6: {"fill_color": RED},
                  11: {"fill_color": RED}
              },
              edge_config={
                  (2, 6): {"stroke_color": RED},
                  (6, 11): {"stroke_color": RED},
                  (11, 2): {"stroke_color": RED}
              }
          )

          # Definir los vértices y bordes para el segundo grafo
        vertices_2 =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        edges_2 = [            
              (0, 1), (1, 2), (2, 3),
              (3, 4), (4, 5), (5, 6),
              (6, 7), (7, 8), (8, 9),
              (9, 10), (10, 11), (11, 0),
              (4, 7), (7, 11), (11, 4)  # Ejemplo de bordes
          ]  
          
          # Crear el segundo grafo con un tamaño más pequeño
        g2 = Graph(
              vertices_2,
              edges_2,
              layout="circular",
              layout_scale=2,  # Reducir el tamaño del grafo
              labels=True,
              vertex_config={
                  4: {"fill_color": BLUE},
                  7: {"fill_color": BLUE},
                  11: {"fill_color": BLUE}
              },
              edge_config={
                  (4, 7): {"stroke_color": BLUE},
                  (7, 11): {"stroke_color": BLUE},
                  (11, 4): {"stroke_color": BLUE}
              }
          )

          # Definir los vértices y bordes para el tercer grafo
        vertices_3 =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        edges_3 = [            
              (0, 1), (1, 2), (2, 3),
              (3, 4), (4, 5), (5, 6),
              (6, 7), (7, 8), (8, 9),
              (9, 10), (10, 11), (11, 0),
              (3, 6), (6, 10), (10, 3)  # Ejemplo de bordes
          ]  
          
          # Crear el tercer grafo con un tamaño más pequeño
        g3 = Graph(
              vertices_3,
              edges_3,
              layout="circular",
              layout_scale=2,  # Reducir el tamaño del grafo
              labels=True,
              vertex_config={
                  3: {"fill_color": GREEN},
                  6: {"fill_color": GREEN},
                  10: {"fill_color": GREEN}
              },
              edge_config={
                  (3, 6): {"stroke_color": GREEN},
                  (6, 10): {"stroke_color": GREEN},
                  (10, 3): {"stroke_color": GREEN}
              }
          )

        title = Text("Inversiones de C").next_to(g2, UP)

          # Ajustar la posición de los grafos para que no se superpongan
        g1.move_to(LEFT * 5)  # Mueve el primer grafo a la izquierda
        g2.next_to(g1, RIGHT)  # Mueve el segundo grafo a la derecha del primero
        g3.next_to(g2, RIGHT)  # Mueve el tercer grafo a la derecha del segundo

          # Añadir los tres grafos a la escena
        # self.add(title, g1, g2, g3)
        self.play(Create(title), Create(g1), Create(g2), Create(g3))

        self.wait(6)
        self.play(Uncreate(title), Uncreate(g1), Uncreate(g2), Uncreate(g3))
      


        text19 = Text("Funciones determinadas").scale(0.6)
        text20 = Text("Paralelas").scale(0.6)
        text21 = Text("Relativas").scale(0.6)
        text22 = Text("Intercambio de la séptima").scale(0.6)
        grupoTexto4 = VGroup(text19, text20, text21, text22).arrange(DOWN).scale(0.6)

        self.play( Create(grupoTexto4), runtime=3)
        self.wait(5)

        self.play(Uncreate(grupoTexto4), runtime=3)
        self.wait(1)
## lo del ejemplo
        text8 = Text("Paralelas Menores").scale(0.9)
        text9 = MathTex(r"p(x) =a, b, c \in \mathcal{Z}_{12} | {a, b+1, c}").scale(0.9)
        text10 = Text("Paralelas Mayor").scale(0.9)
        text11 = MathTex(r"P(x) =A, B, C \in \mathcal{Z}_{12} | {a, b-1, c}").scale(0.9)

        text8.set_color(RED)
        text10.set_color(GREEN)

        grupoTextoMayor = VGroup(text8, text9).arrange(DOWN)
        grupoTextoMenor = VGroup(text10, text11).arrange(DOWN)
        grupoParalelas = VGroup(grupoTextoMayor, grupoTextoMenor).arrange(RIGHT).scale(0.6)

        self.play( Create(grupoParalelas), runtime=3)
        self.wait(5)

        text8 = Text("Intercambio de la séptima  Menores").scale(0.9)
        text9 = MathTex(r"p(x) =a, b, c \in \mathcal{Z}_{12} | {c+1, a, b}").scale(0.9)
        text10 = Text("Intercambio de la séptima  Mayor").scale(0.9)
        text11 = MathTex(r"P(x) =A, B, C \in \mathcal{Z}_{12} | {B, C, A-1}").scale(0.9)

        text8.set_color(RED)
        text10.set_color(GREEN)

        grupoTextoMayor = VGroup(text8, text9).arrange(DOWN)
        grupoTextoMenor = VGroup(text10, text11).arrange(DOWN)
        gruposeptima = VGroup(grupoTextoMayor, grupoTextoMenor).arrange(RIGHT).scale(0.6)

        self.play( Uncreate(grupoParalelas), Create(gruposeptima), runtime=3)
        self.wait(5)

        text8 = Text("Relativas Menores").scale(0.9)
        text9 = MathTex(r"p(x) =a, b, c \in \mathcal{Z}_{12} | {b, c, a-2}").scale(0.9)
        text10 = Text("Relativas Mayor").scale(0.9)
        text11 = MathTex(r"P(x) =A, B, C \in \mathcal{Z}_{12} | {B, A, C+2}").scale(0.9)

        text8.set_color(RED)
        text10.set_color(GREEN)

        grupoTextoMayor = VGroup(text8, text9).arrange(DOWN)
        grupoTextoMenor = VGroup(text10, text11).arrange(DOWN)
        grupoRelativas = VGroup(grupoTextoMayor, grupoTextoMenor).arrange(RIGHT).scale(0.6)

        self.play(  Uncreate(gruposeptima),Create(grupoRelativas), runtime=3)
        self.wait(5)
        self.play(  Uncreate(grupoRelativas), runtime=3)

        textoParalela = MathTex(r"P(c) = P ({0, 3, 7}) = {0, 4, 7} = C  \quad P (F) = P ({5, 9, 0}) = {5, 8, 0} = f").scale(0.9)
        textoSeptima =MathTex(r"L(e) = L({4, 7, 11}) = {0, 4, 7} = C   \quad L(G) = L({7, 11, 2}) = {11, 2, 6} = b").scale(0.9)
        textoRelativa = MathTex(r"R(b) = R({11, 2, 6}) = {2, 6, 9} = D   \quad R(A) = R({9, 1, 4}) = {6, 1, 9} = f\#").scale(0.9)
        grupoEjemplo = VGroup(textoParalela, textoSeptima, textoRelativa).arrange(DOWN)

        self.play( Create(grupoEjemplo), runtime=3)
        self.wait(15)
        self.play( Uncreate(grupoEjemplo), runtime=3)




### metodo para el Tonnetz
    def Tonnetz(self):
      ## parametros
        spacing = 1.5 
        rows, cols = 6, 6  
        offset = 0.6  # espaciado

        # Matriz de notas en la estructura de Tonnetz
        notes = [
            [11, 6, 1, 8, 3, 10],
            [2, 9, 4, 11, 6, 1],
            [10, 5, 0, 7, 2, 9],
            [1, 8, 3, 10, 5, 0],
            [9, 4, 11, 6, 1, 8],
            [0, 7, 2, 9, 4, 11]
        ]

        # Crear el grupo de puntos y etiquetas
        lattice_points = VGroup()
        labels = VGroup()

        # Añadir puntos y etiquetas
        for i in range(rows):
            for j in range(cols):
                # Calcular posición de cada punto
                x = j * spacing + (i % 2) * offset
                y = -i * spacing * 0.75
                point = Dot(point=[x, y, 0], color=WHITE, radius=0.2)  # Punto más pequeño
                lattice_points.add(point)

                # Agregar etiqueta de nota
                note = notes[i][j]
                label = MathTex(f"{note}").scale(0.8).move_to(point.get_center())
                label.set_color(RED)  # Escala de etiqueta más pequeña
                labels.add(label)

        # Agrupar puntos y etiquetas, y centrar en la pantalla
        lattice_group = VGroup(lattice_points, labels)
        lattice_group.move_to(ORIGIN)

        # Crear y agregar las conexiones entre puntos ajustadas al centro
        edges = VGroup()  # Grupo para las líneas de conexión

        for i in range(rows):
            for j in range(cols):
                # Índice del punto actual
                current_index = i * cols + j
                current_point = lattice_points[current_index]

                # Conectar al punto superior
                if i > 0:
                    above_point = lattice_points[(i - 1) * cols + j]
                    edges.add(Line(current_point.get_center(), above_point.get_center(), stroke_width=1))

                # Conectar al punto de la izquierda
                if j > 0:
                    left_point = lattice_points[i * cols + (j - 1)]
                    edges.add(Line(current_point.get_center(), left_point.get_center(), stroke_width=1))

                # Conectar al punto superior izquierdo (diagonal)
                if i > 0 and j > 0:
                  if(i % 2 ==0):
                      top_left_point = lattice_points[(i - 1) * cols + (j - 1)]
                      print(current_point.get_center())
                      print("simon", top_left_point.get_center())
                      edges.add(Line(current_point.get_center(), top_left_point.get_center(), stroke_width=1))
                # Conectar al punto superior derecho (diagonal)

            # Conectar al punto superior derecho (diagonal)
                if i > 0 and j < cols - 1:
                    if(i % 2 !=0):
                      top_right_point = lattice_points[(i - 1) * cols + (j + 1)]
                      edges.add(Line(current_point.get_center(), top_right_point.get_center(), stroke_width=1))


        # Agregar puntos, etiquetas y conexiones a la escena
        self.play(FadeIn( edges), runtime = 3)
        self.wait(4)
        self.play(FadeIn( lattice_group), runtime = 3)
        self.wait(4)
        self.play(FadeOut( lattice_group, edges), runtime = 3)
        self.wait(1)


    def novenaSinfonia(self):
      textoIntroductorio = Text("Esto genera un lattice")
    def videoToro(self):
          ## losta de videos
              videoToro = VideoMobject(
                  filename=r"/content/videos/toroTonnetz.mp4",
                  speed=0.5
              ).scale_to_fit_width(5).to_corner(UL)
            
              v1 = Group(videoToro, SurroundingRectangle(videoToro))
   
              self.wait(10)
      ### visualizacion rapida de uno de ellos y fragmento de codigo
              self.play((v1.animate.shift(RIGHT*3+DOWN*3).scale(2)), run_time = 5)
              self.remove(v1)



#############################################################
### clase para el toro del tonnetz

class toroTonnetz(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        torus = Torus()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(axes))
        self.play(Create(torus))
        
        self.begin_ambient_camera_rotation(rate = 3)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.play(Uncreate(torus))
        self.play(Uncreate(axes))



