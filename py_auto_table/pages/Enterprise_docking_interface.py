import streamlit as st
from utilics import runMakeEnterprise
import time

curtime = time.localtime()
st.title(f"{curtime[0]}学年学生助理企业对接系统")
st.video("py_auto_table/videos/entireweb1.mp4",start_time=0,autoplay=True,loop=True)
st.divider()
columns1,columns2 = st.columns(2)
with columns1:
    file_enterprise = st.file_uploader("(๑• . •๑)请上传🎈企业数据表🎈",key=1)
st.divider()
with columns2:
    file_worker = st.file_uploader("(๑• . •๑)请上传🎈助理值班表🎈",key=2)

if file_enterprise and file_worker:
    with st.spinner("正在加载中...."):
        time.sleep(2)
        enterprise = runMakeEnterprise(file_enterprise,file_worker)
    st.snow()
    st.data_editor(enterprise,hide_index=True)

st.subheader("๐•ᴗ•๐ 企业排表注意事项")
st.divider()
st.markdown(
    """
    1.只用安排蛟桥的在大活的宣讲会。\n
    2.安排的对接助理一般为对应的组长和组员。
    """
)