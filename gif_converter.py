from moviepy.editor import VideoFileClip

def convert_video_to_gif(input_file, output_file, fps=10, fuzz=5):
    """
    mp4動画をGIFアニメーションに変換する関数
    
    Parameters:
    - input_file (str): 入力するmp4動画のファイル名
    - output_file (str): 出力するGIFアニメーションのファイル名
    - fps (int): GIFアニメーションのフレームレート（デフォルト: 10）
    - fuzz (int): ImageMagickのfuzzオプションの値（デフォルト: 5）
    """
    # mp4動画を読み込む
    clip = VideoFileClip(input_file)
    
    # 動画の長さを取得
    duration = clip.duration
    
    # 最後のフレームを除外するために、動画の一部分を切り出す
    subclip = clip.subclip(0, duration - 0.1)  # 最後の0.1秒を除外
    
    # GIFアニメーションに変換（軽量化）
    # subclip.write_gif(output_file, fps=fps, program='ImageMagick', opt='OptimizeTransparency', fuzz=fuzz, verbose=False)
    subclip.write_gif(output_file, fps=fps, opt='OptimizeTransparency', fuzz=fuzz, verbose=False)
    
    # メモリを解放
    clip.close()
    subclip.close()

if __name__ == '__main__':
    # 使用例
    input_file = 'cat2.mp4'
    output_file = 'output_animation.gif'
    convert_video_to_gif(input_file, output_file, fps=12, fuzz=10)