import streamlit as st
import os
from gif_converter import convert_video_to_gif

# docs\page_front.mdファイルの内容を読み込む
if os.path.exists("docs/page_front.md"):
    with open("docs/page_front.md", "r", encoding="utf-8") as f:
        page_front_content = f.read()
        st.markdown(page_front_content, unsafe_allow_html=True)

def main():

    # GIFアニメーションに変換するパラメータを設定
    with st.sidebar:
        fps = st.slider("Select FPS", min_value=1, max_value=30, value=15, step=1)
        program = st.selectbox("Select program", ["imageio"], index=0)
        opt = st.selectbox("Select optimization", ["OptimizeTransparency", "optimizeplus"], index=0)
        fuzz = st.slider("Select fuzz", min_value=1, max_value=20, value=10, step=1)
    
    # ユーザーからmp4動画をアップロードしてもらう
    uploaded_file = st.file_uploader("Choose an MP4 file", type="mp4")
    
    if uploaded_file is not None:
        # アップロードされたファイルを一時的に保存
        with open("temp.mp4", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        if st.button("Convert"):
            # GIFアニメーションに変換
            output_file = "output.gif"
            with st.spinner('Wait for it...'):
                convert_video_to_gif("temp.mp4", output_file, fps=fps, program=program, opt=opt, fuzz=fuzz)
            
            # 変換後のGIFアニメーションを表示
            st.success("Conversion complete!")
            with open(output_file, "rb") as f:
                bytes_data = f.read()
            st.download_button(label="Download GIF", data=bytes_data, file_name="output.gif", mime="image/gif")
            
            # 一時ファイルを削除
            os.remove("temp.mp4")
            os.remove(output_file)

if __name__ == "__main__":
    main()