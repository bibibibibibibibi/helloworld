import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

st.header(':red[st.write]',divider='rainbow')
st.subheader('This is a _subheader_ :sunglasses:')
st.caption('This is a string that explains somthing above')
st.write('Hello, *World!*:sunglasses:')

st.write(1234)

df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})
st.write(df)


st.write('Below is a DataFrame:',df,"Above is a datafram.")

df2=pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)
c=alt.Chart(df2).mark_circle().encode(
    x='a',y='b',size='c',color='c',tooltip=['a','b','c']
)
st.write(c)

md=st.text_area('Type in your markdown string (without outer quotes)',"Happy strealit-ing! :balloon:")
mdd=st.text('''Type in your markdown string (without outer quotes) Happy strealit-ing! :balloon:''')


st.markdown(md)
st.markdown('''Type in your markdown string (without outer quotes) Happy strealit-ing! :balloon:''')

st.code(f"""
        import streamlit as st
        st.markdown('''{md}''')
        """
)

st.code('''def hello():
        print("Hello, streamlit")''', language='python')

st.latex(r''' -i\hbar\frac{\partial\psi}{\partial t}=\hat{H}\psi''')