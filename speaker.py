from speakerpy.lib_speak import Speaker
from speakerpy.lib_sl_text import SeleroText

text = SeleroText("Пример текста для синтеза речи", to_language='ru')
speaker = Speaker(model_id="ru_v3", language="ru", speaker="aidar", device="cpu")
speaker.speak(text=text, sample_rate=48000, speed=1.0)