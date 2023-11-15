%%manim -v WARNING -qm KSPLogo
class KSPLogo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        List = c1, c2, c3, c4, c5 = [Circle(radius=0.95, color=BLACK) for _ in range(5)]
        up=c1, c3, c5
        down= c2, c4
        i=0
        colour=[BLUE,YELLOW,BLACK,GREEN,RED,]
        for c in List:
            i+=1
            c.move_to((i,0,0))
            self.play(c.animate)
        for c in up:
            self.play(c.animate.shift(UP*0.25))
        for c in down:
            self.play(c.animate.shift(DOWN*0.25))
        for c,co in List,colour:
            self.play(c.animate.set_color(colour))
