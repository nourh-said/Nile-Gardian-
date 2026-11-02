from pathlib import Path
import html as h
import gradio as gr

game = (Path(__file__).parent / "game.html").read_text(encoding="utf-8")
iframe = f'<iframe srcdoc="{h.escape(game, quote=True)}" style="width:100%;height:92vh;border:0" allow="autoplay"></iframe>'

with gr.Blocks(title="مغامرة حارس النيل العجيب") as demo:
    gr.HTML(iframe)

demo.launch(share=True)