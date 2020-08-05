<template>
    <div>
        <el-input :placeholder=elinputplace v-model="q" class="input-with-select">
            <el-button slot="append" type="primary" plain @click="search" icon="el-icon-search">{{$t('msg.search')}}</el-button>
        </el-input>

        <el-dialog :title=eltitle :visible.sync="dialogVisible">
            <h4>{{$t('msg.nothing')}}{{q}}</h4>
            <Hot @childevent="emitm"></Hot>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">{{$t('msg.cancel')}}</el-button>
                <el-button type="primary" @click="openaddhot">{{$t('msg.add')}}</el-button>
            </span>
        </el-dialog>

        <el-dialog :title=eltitle :visible.sync="dialogVisible2">
            <h4>{{$t('msg.addq')}}</h4>
                <el-input v-model="q"></el-input>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible2 = false">{{$t('msg.cancel')}}</el-button>
                <el-button type="primary" @click="addhot">{{$t('msg.add')}}</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
    import Hot from "@/components/Hot";
    export default {
        components:{Hot},
        name: "SearchItem",
        computed:{
            elinputplace(){return this.$t('msg.searchkey')},
            eltitle(){return this.$t('msg.notice')}
        },
        data(){
            return{
                ans:'',
                q:'',
                author:'',
                dialogVisible:false,
                dialogVisible2:false
            }
        },
        methods:{
            emitm(str){
                this.$emit("childevent",str)
                this.dialogVisible=false
            },
            search(){
                console.log(this.q)
                if(this.q=='') return
                this.$axios.get('http://47.95.199.35:8000/search',{
                    params: {q:this.q}
                }).then((response) => {
                    if(response.data.count > 0){
                        console.log("aasdfasdfasdf")
                        this.$router.replace('/index/result/'+this.q)
                        this.$emit("childevent",this.q)
                    }else{
                        this.dialogVisible = true
                    }

                }).catch(() => {

                });
            },
            openaddhot(){
                this.dialogVisible = false  // 关闭第一个提示框
                this.dialogVisible2 = true  // 打开第二个提示框
            },
            addhot(){
                this.dialogVisible2 = false
                this.$axios.get('http://47.95.199.35:8000/addques',{
                    params: {q:this.q,ans:this.ans,author:'Jany'}
                }).then((response) => {
                    if(response.status==200){
                        this.$message(this.$t('msg.add')+this.$t('msg.success'));
                    }
                }).catch(() => {

                });
            }
        }
    }
</script>

<style scoped>
    .el-dialog{
        width: 60%;
    }
</style>