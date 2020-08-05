<template>
    <div>
        <el-container >
            <Navigate/>
            <el-main :class="my_style" :style="defaultHeight"><router-view/></el-main>
            <el-footer ref="myfooter">
                <div class="footer">
                    <strong class="word">{{$t('footer.email')}}TheHub@nottingham.edu.cn &nbsp;&nbsp;</strong><br>
                    <strong class="word">{{$t('footer.telephone')}}+86 (0)574 8818 0000 &nbsp;&nbsp;</strong>
                    <strong class="word">{{$t('footer.telephone')}}+86 (0)574 8818 9372 &nbsp;&nbsp;</strong>
                </div>
            </el-footer>
        </el-container>
    </div>
</template>

<script>
    import Navigate from "@/components/Navigate";
    export default {
        name: "Display",
        components:{Navigate},
        data(){
            return {
                my_style:'my-el-main2',
                defaultHeight: {
                    height: ""
                }
            }
        },
        methods:{
            init_fuc(){
                this.defaultHeight.height = window.innerHeight - 120 + "px"
                if(this.$route.path.includes('search')){
                    this.my_style = 'my-el-main1'
                }else{
                    this.my_style = 'my-el-main2'
                }
            }
        },
        beforeUpdate(){
            this.init_fuc()
        },
        created(){
            this.init_fuc()
        }
    }
</script>

<style scoped>
    .my-el-main1{
        background-image: url("../assets/bg1.jpg");
        /*height: 720px;*/
    }
    .my-el-main2{
        background-color: #ededed;
        /*height: 720px;*/
    }
    .el-footer{
        background-color: #545C64;
    }
    .footer{
        text-align: center;
        margin-top: 10px;
        color: white;
    }
</style>