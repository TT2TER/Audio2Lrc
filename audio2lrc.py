import sys,whisper,swapsub,os
from datetime import datetime
from whisper.utils import write_srt

if __name__ == '__main__' :
    if len(sys.argv) > 3 or len(sys.argv) == 1:
        print("[ERROR]  Invalid parameter, using as following:\n",
                "audio2lrc <audio path> <reserve srt or not>")
    else :
        # whisper转录
        # 可选模型请见https://github.com/openai/whisper#available-models-and-languages
        # 请用链接中选项替换，默认base
        tic = datetime.now()
        model = whisper.load_model("base")
        result = model.transcribe(sys.argv[1])
        toc = datetime.now()
        print("Transcription completed!\n")
        print(result["text"])
        #读取文件名
        name=os.path.splitext(sys.argv[1])[0]
        #生成临时文件.srt
        with open(name + ".srt", "w", encoding="utf-8") as srt:
            write_srt(result["segments"], file=srt)
        #生成lrc文件
        srt_ = swapsub.load(name + ".srt")
        
        print(name,"\n")
        swapsub.convert(srt_, name+".lrc")
        if len(sys.argv)==2:
            os.remove(name + ".srt")
        else:
            print("srt has been exported at",name+".srt\n")
        print("lrc has been exported at",name+".lrc")
        print('\ntotal time: %f seconds\n' % (toc-tic).total_seconds())