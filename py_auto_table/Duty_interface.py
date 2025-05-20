import streamlit as st
from utilics import runUtilics
import time

#video_file = open("py_auto_table\videos\web1.mp4","rb")
#video_bytes = video_file.read()
curtime = time.localtime()

with st.sidebar:
    st.title("๐•ᴗ•๐ 招就处排班注意事项")
    st.divider()
    st.subheader("๐•ᴗ•๐ 排表事宜")
    st.markdown(
        """
    1、早上值班人员最多3人(最好2人)，下午时间段最多4人(最好3人)，晚班最好2人。\n
    2、新助理和勤工岗人员优先每周排两个时间段，在人数够的情况下，老助理一周一个时间段即可(尽量多给新人锻炼机会）。\n
    3、每个班次，必须至少需要安排老助理值班(除非该时间段无老助理)。\n
    4、值班初表***周四***发送到总群中(发送前，先给排班负责人检查)， ***周五***发送最终版到总群，最终版确定以后，还需制作***签到表***，发送给每周一对应的组长。\n
    5、有需要更改值班时间的助理，接收消息后，需要告知其他负责排班的小助理，便于修改对应的无课时间。\n
    6、发完最终表，需要制作 ***签到表***发给***周一***值班的组长，注意更改***签到时间！！！！***
        """
    )
    st.subheader("๐•ᴗ•๐ 排表附加事项")
    st.write(
        """
    1、需要手动从周一至周五任意选一天从某一班次(最好是早上、下午、晚上的***最后一班或者第一个班次***)的小组长负责本周***办公室和接待室***卫生打扫，尽量每位助理轮着来。(每周的安排可以按照 ***13542***来，***也就是周一、周三、周五、周四、周二***)\n
    2、每周都需要安排助理打扫面试间，小面试间安排一个人打扫，大面试间(3号，8号)安排两人打扫。一般安排***早上第一班助理***打扫一个面试间，***下午第二班助理***打扫一个面试间。**需要注意的是**，有安排打扫办公室的那天可以不用安排助理打扫面试间。
        """
    )


st.title(f"{curtime[0]}学年招就处学生助理排班系统")

st.video("py_auto_table/videos/entireweb2.mp4",start_time=0,autoplay=True,loop=True)

st.divider()

st.subheader("🎈设置各班人员数🎈")

columns1,columns2 = st.columns(2)
#设置每个时间段值班人数
with columns1:
    to_one = st.slider("๐•ᴗ•๐ 早上第一班(1-2)值班人数",min_value=1,max_value=3,step=1,value=2)
    to_two = st.slider("๐•ᴗ•๐ 早上第二班(3-5)值班人数",min_value=2,max_value=4,step=1,value=3)
    nx_one = st.slider("๐•ᴗ•๐ 下午第一班(6-7)值班人数",min_value=1,max_value=3,step=1,value=2)
with columns2:
    nx_two = st.slider("๐•ᴗ•๐ 下午第二班(8-9)值班人数",min_value=2,max_value=4,step=1,value=3)
    night = st.slider("๐•ᴗ•๐ 晚上值班(10-11)人数",min_value=0,max_value=2,step=1,value=2)
st.divider()
#获取上传的文件
upload_file = st.file_uploader("๐•ᴗ•๐ 请上传人员数据表(200MB以内),仅支持excel格式",type=["xlsx","csv"])
#将三个表格置于不同的tab中
tableofworker,tableofstatics,tableofwarning = st.tabs(["值班助理工作表","值班助理统计数据表","排班警告提示表"])

#判断是否上传文件
if upload_file:
    with st.spinner("正在加载中...."):
        df_worker,df_statics,df_warning = runUtilics(upload_file,to_one,to_two,nx_one,nx_two,night)
    st.balloons()
#显示值班表数据
with tableofworker:
    if upload_file:
        st.write("๐•ᴗ•๐ 程序生成值班表")
        #这里的.T使得原本数据表格中，行和列互换了
        st.table(df_worker.T)
        st.divider()
        st.write("๐•ᴗ•๐ 待修改值班表(若无任何警告，可无需修改，直接下载即可)")
        st.data_editor(df_worker.T)
    else:
        st.write("๐•ᴗ•๐ 内容为空，请上传文件！")
with tableofstatics:
    if upload_file:
        st.dataframe(df_statics,hide_index=True)
    else:
        st.write("๐•ᴗ•๐ 内容为空，请上传文件！")
with tableofwarning:
    if upload_file:
        st.dataframe(df_warning,hide_index=True)
    else:
        st.write("๐•ᴗ•๐ 内容为空，请上传文件！")

   
    

