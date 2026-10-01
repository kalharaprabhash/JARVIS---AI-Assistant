import tkinter as tk
import math
import time
import random


WIDTH = 1280
HEIGHT = 720


class JarvisHUD:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("JARVIS")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.configure(bg="#020409")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=WIDTH,
            height=HEIGHT,
            bg="#020409",
            highlightthickness=0
        )

        self.canvas.pack()

        self.angle = 0
        self.mouth_phase = 0
        self.speaking = False

        self.build_background()
        self.build_hud()
        self.build_iron_face()
        self.build_voice_panel()

        self.animate()

    # ==================================================
    # BACKGROUND
    # ==================================================

    def build_background(self):

        # Grid
        for x in range(0, WIDTH, 40):
            self.canvas.create_line(
                x, 0, x, HEIGHT,
                fill="#061018"
            )

        for y in range(0, HEIGHT, 40):
            self.canvas.create_line(
                0, y, WIDTH, y,
                fill="#061018"
            )

        # Outer frame
        self.canvas.create_rectangle(
            18, 18,
            WIDTH - 18,
            HEIGHT - 18,
            outline="#07506a",
            width=2
        )

        # Corner lines
        corners = [
            (25, 25, 130, 25),
            (25, 25, 25, 100),

            (1150, 25, 1255, 25),
            (1255, 25, 1255, 100),

            (25, 695, 130, 695),
            (25, 620, 25, 695),

            (1150, 695, 1255, 695),
            (1255, 620, 1255, 695)
        ]

        for x1, y1, x2, y2 in corners:
            self.canvas.create_line(
                x1, y1, x2, y2,
                fill="#00a9d0",
                width=3
            )

    # ==================================================
    # HUD
    # ==================================================

    def build_hud(self):

        self.canvas.create_text(
            640,
            42,
            text="J A R V I S",
            fill="#00d9ff",
            font=("Arial", 28, "bold")
        )

        self.canvas.create_text(
            640,
            72,
            text="NEURAL ASSISTANT INTERFACE",
            fill="#426b78",
            font=("Consolas", 9)
        )

        self.status = self.canvas.create_text(
            1120,
            45,
            text="● SYSTEM ONLINE",
            fill="#00ff9d",
            font=("Consolas", 10, "bold")
        )

    # ==================================================
    # IRON MAN FACE
    # ==================================================

    def build_iron_face(self):

        cx = 640
        cy = 350

        # Holographic outer rings
        self.ring1 = self.canvas.create_oval(
            375, 105,
            905, 635,
            outline="#06384a",
            width=2
        )

        self.ring2 = self.canvas.create_oval(
            405, 135,
            875, 605,
            outline="#07586e",
            width=1
        )

        self.arc1 = self.canvas.create_arc(
            350, 80,
            930, 650,
            start=0,
            extent=70,
            outline="#00cfff",
            width=3,
            style=tk.ARC
        )

        self.arc2 = self.canvas.create_arc(
            380, 110,
            900, 620,
            start=180,
            extent=90,
            outline="#00ff9d",
            width=2,
            style=tk.ARC
        )

        # ------------------------------------------------
        # HELMET SILHOUETTE
        # ------------------------------------------------

        helmet = [
            505, 175,
            550, 145,
            640, 130,
            730, 145,
            775, 175,

            815, 225,
            825, 310,
            805, 410,

            765, 485,
            715, 535,
            640, 560,

            565, 535,
            515, 485,
            475, 410,

            455, 310,
            465, 225
        ]

        self.canvas.create_polygon(
            helmet,
            fill="#5b1b13",
            outline="#b84a24",
            width=3
        )

        # ------------------------------------------------
        # GOLD FACE PLATE
        # ------------------------------------------------

        face = [
            540, 205,
            590, 180,
            690, 180,
            740, 205,

            765, 260,
            755, 370,

            725, 440,
            680, 485,

            640, 500,

            600, 485,
            555, 440,

            525, 370,
            515, 260
        ]

        self.canvas.create_polygon(
            face,
            fill="#b87922",
            outline="#e6b94a",
            width=3
        )

        # ------------------------------------------------
        # SIDE ARMOR
        # ------------------------------------------------

        self.canvas.create_polygon(
            475, 230,
            515, 205,
            525, 370,
            500, 430,
            475, 390,
            fill="#7c2919",
            outline="#c65b2c",
            width=2
        )

        self.canvas.create_polygon(
            805, 230,
            765, 205,
            755, 370,
            780, 430,
            805, 390,
            fill="#7c2919",
            outline="#c65b2c",
            width=2
        )

        # ------------------------------------------------
        # EYES
        # ------------------------------------------------

        self.left_eye = self.canvas.create_polygon(
            535, 265,
            585, 250,
            615, 265,
            580, 282,
            540, 278,
            fill="#dfffff",
            outline="#00eaff",
            width=2
        )

        self.right_eye = self.canvas.create_polygon(
            665, 265,
            695, 250,
            745, 265,
            740, 278,
            700, 282,
            fill="#dfffff",
            outline="#00eaff",
            width=2
        )

        # Eye glow lines
        self.left_glow = self.canvas.create_line(
            540, 290,
            610, 290,
            fill="#00bde8",
            width=2
        )

        self.right_glow = self.canvas.create_line(
            670, 290,
            740, 290,
            fill="#00bde8",
            width=2
        )

        # ------------------------------------------------
        # NOSE
        # ------------------------------------------------

        self.canvas.create_polygon(
            625, 280,
            655, 280,
            665, 365,
            640, 390,
            615, 365,
            fill="#9d641e",
            outline="#dba43b",
            width=2
        )

        # ------------------------------------------------
        # JAW
        # ------------------------------------------------

        jaw = [
            555, 405,
            590, 435,
            640, 450,
            690, 435,
            725, 405,
            710, 480,
            670, 515,
            640, 525,
            610, 515,
            570, 480
        ]

        self.canvas.create_polygon(
            jaw,
            fill="#76291a",
            outline="#bd512a",
            width=3
        )

        # ------------------------------------------------
        # MOUTH / SPEAKING ANIMATION
        # ------------------------------------------------

        self.mouth = self.canvas.create_polygon(
            610, 455,
            640, 448,
            670, 455,
            655, 468,
            640, 472,
            625, 468,
            fill="#080b0e",
            outline="#d58a32",
            width=2
        )

        # Mouth light
        self.mouth_light = self.canvas.create_line(
            620, 455,
            660, 455,
            fill="#00d9ff",
            width=1
        )

        # Face label
        self.face_status = self.canvas.create_text(
            640,
            590,
            text="JARVIS NEURAL CORE",
            fill="#008caf",
            font=("Consolas", 10, "bold")
        )

    # ==================================================
    # VOICE PANEL
    # ==================================================

    def build_voice_panel(self):

        # Left
        self.canvas.create_text(
            60,
            155,
            text="SYSTEM",
            anchor="w",
            fill="#00d9ff",
            font=("Consolas", 12, "bold")
        )

        self.canvas.create_text(
            60,
            195,
            text="CPU       42%",
            anchor="w",
            fill="#77929c",
            font=("Consolas", 10)
        )

        self.canvas.create_text(
            60,
            225,
            text="MEMORY    58%",
            anchor="w",
            fill="#77929c",
            font=("Consolas", 10)
        )

        self.canvas.create_text(
            60,
            255,
            text="BATTERY   87%",
            anchor="w",
            fill="#77929c",
            font=("Consolas", 10)
        )

        # Right
        self.canvas.create_text(
            1010,
            155,
            text="VOICE",
            anchor="w",
            fill="#00d9ff",
            font=("Consolas", 12, "bold")
        )

        self.voice_state = self.canvas.create_text(
            1010,
            195,
            text="MIC READY",
            anchor="w",
            fill="#00ff9d",
            font=("Consolas", 10, "bold")
        )

        self.command_text = self.canvas.create_text(
            1010,
            235,
            text="COMMAND: ---",
            anchor="w",
            fill="#77929c",
            font=("Consolas", 9)
        )

        self.response_text = self.canvas.create_text(
            1010,
            275,
            text="RESPONSE: READY",
            anchor="w",
            fill="#77929c",
            font=("Consolas", 9)
        )

        # Waveform
        self.wave = []

        for i in range(12):

            bar = self.canvas.create_rectangle(
                1010 + i * 18,
                340,
                1020 + i * 18,
                350,
                fill="#008cab",
                outline=""
            )

            self.wave.append(bar)

    # ==================================================
    # ANIMATION
    # ==================================================

    def animate(self):

        self.angle += 3
        self.mouth_phase += 0.25

        # Rotating holographic rings

        self.canvas.itemconfig(
            self.arc1,
            start=self.angle
        )

        self.canvas.itemconfig(
            self.arc2,
            start=-self.angle
        )

        # Speaking animation
        if self.speaking:

            opening = 5 + abs(
                math.sin(self.mouth_phase)
            ) * 18

            self.canvas.coords(
                self.mouth,
                610, 455,
                640, 448 - opening,
                670, 455,
                655, 468 + opening,
                640, 472 + opening,
                625, 468 + opening
            )

            self.canvas.itemconfig(
                self.voice_state,
                text="● JARVIS SPEAKING",
                fill="#00d9ff"
            )

        else:

            self.canvas.coords(
                self.mouth,
                610, 455,
                640, 448,
                670, 455,
                655, 468,
                640, 472,
                625, 468
            )

            self.canvas.itemconfig(
                self.voice_state,
                text="● MICROPHONE READY",
                fill="#00ff9d"
            )

        # Waveform

        for i, bar in enumerate(self.wave):

            height = 8 + abs(
                math.sin(
                    self.angle / 8 + i
                )
            ) * 35

            x = 1010 + i * 18

            self.canvas.coords(
                bar,
                x,
                350 - height,
                x + 10,
                350
            )

        # Online indicator

        if int(time.time() * 2) % 2 == 0:

            self.canvas.itemconfig(
                self.status,
                fill="#00ff9d"
            )

        else:

            self.canvas.itemconfig(
                self.status,
                fill="#007d63"
            )

        self.root.after(
            30,
            self.animate
        )

    # ==================================================
    # TEST SPEAKING MODE
    # ==================================================

    def test_speaking(self):

        self.speaking = not self.speaking

        self.root.after(
            2000,
            self.stop_speaking
        )

    def stop_speaking(self):

        self.speaking = False

    # ==================================================
    # RUN
    # ==================================================

    def run(self):

        # Press SPACE to test speaking animation

        self.root.bind(
            "<space>",
            lambda event: self.test_speaking()
        )

        self.root.mainloop()


if __name__ == "__main__":

    app = JarvisHUD()
    app.run()