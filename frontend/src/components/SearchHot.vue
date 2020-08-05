<template>
    <div>
        <el-card class="my-card"
                 v-for="(item,index) in items"
                 :key="index"
                 >
            <el-image @click="gethot(item.label)"
                    :src=item.url
            ></el-image>
                <span class="my-word" @click="gethot(item.label)">{{item.label}}</span>
        </el-card>
    </div>
</template>

<script>
    export default {
        name: "SearchHot",
        data(){
            return{
                items: [
                    { type: 'info', label: 'Loading',url:require("@/assets/hot/work.png") },
                    { type: 'info', label: 'Loading',url:require("@/assets/hot/miss_work.png")},
                    { type: 'info', label: 'Loading',url:require("@/assets/hot/course.png")},
                    { type: 'info', label: 'Loading',url:require("@/assets/hot/sick.png")},
                    { type: 'info', label: 'Loading',url:require("@/assets/hot/study.png")}
                ],
                currentDate: new Date()
            }
        },
        created:function () {
            console.log(123)
            console.log("1234")
            this.$axios.get('http://47.95.199.35:8000/hot/').then((response) => {
                let data = response.data.slice(1,-1).split(', ')
                for(let i = 0;i < 5;i++){
                    this.items[i].label = data[i].slice(1,-1)
                }
            }).catch(() => {
            });
        },
        methods:{
            gethot(label){
                // this.$router.replace('/index/result/'+label)
                this.$emit("childevent",label)
                this.$router.replace('/index/result/'+label)
            }
        }
    }
</script>

<style scoped>
    .el-card{
        width: 120px;
        height: 100px;
        float: left;
        margin-top: 4%;
        margin-left: 6%;
        background-color: #ecf5ff;
    }
    .my-card >>> .el-card__body{
        padding: 1px;
        text-align: center;
    }
    .my-word{
        display: block;
        font-size: 13px;
    }
    .el-image{
        text-align: center;
        width: 50px;
        height: 50px;
        margin: 10px;
    }

</style>