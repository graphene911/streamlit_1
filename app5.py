import streamlit as st
import pandas as pd

# 이미지 처리를 위한 라이브러리
from PIL import Image

def main() :
    # 1. 저장되어있는, 이미지 파일을 화면에 표시하기
    img = Image.open('data2/image_03.jpg')
    
    st.image(img)
    st.image(img, use_column_width=True)

    # 2. 인터넷상에 있는 이미지를 화면에 표시하기
    #    url이 있는 이미지를 말한다.
    url = 'https://www.spcmagazine.com/wp-content/uploads/2019/07/%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%B0%B0%EC%8A%A4%ED%82%A8%EB%9D%BC%EB%B9%88%EC%8A%A4_-%EC%9D%B8%EA%B8%B0-%ED%94%8C%EB%A0%88%EC%9D%B4%EB%B2%84-2%EC%A2%85-%EC%9E%AC%EC%B6%9C%EC%8B%9C.jpg'

    st.image(url)

    # 3. video파일을 화면에 표시하기
    video_file = open('data2/secret_of_success.mp4', 'rb')

    st.video(video_file)

    audio_file = open('data2/song.mp3', 'rb')

    st.audio(audio_file.read(), format='audio/mp3' )



if __name__ == '__main__' :
    main()