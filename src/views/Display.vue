<template>
    <div>
        <el-container >
            <Navigate/>
            <el-main><router-view/></el-main>
            <el-footer>
                <div class="footer">
                    {{foot_msg}}
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
                foot_msg:'我是底部信息，可以从后端获得或者写死'
            }
        }
    }
</script>

<style scoped>
    .el-main{
        background-color: #ededed;
        height: 700px;
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