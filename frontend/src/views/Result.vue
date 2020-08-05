<template>
    <div>
        <div id="left">
            <div class="searchBox">
                <search-item @childevent="eventget"></search-item>
            </div>
            <el-collapse>
                <div class="test"
                     v-for="(item,index) in res"
                     :key="index">
                    <el-card shadow="always">
                        <el-collapse-item
                                :title="item.ques"
                                :key="index"
                                class="my-col-item">
                            <h4>{{item.ans}}</h4>
                        </el-collapse-item>
                        <div id="left-in">
                            <p>{{$t('other.author')}}:{{item.author}}</p>
                        </div>
                        <div id = "right">
                            <el-tag type="success"
                                    effect="dark"
                                    size="small"
                                    @click.native="addA(item.id)"
                                    v-show="item.ans==''">{{$t('msg.adda')}}</el-tag>
                        </div>
                    </el-card>
                </div>
            </el-collapse>
        </div>

        <el-dialog :title=eltitle :visible.sync="dialogVisible2">
            <h4>{{$t('msg.adda')}}:</h4>
            <el-input v-model="ans"></el-input>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible2 = false">{{$t('msg.cancel')}}</el-button>
                <el-button type="primary" @click="addans">{{$t('msg.add')}}</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
    import SearchItem from "@/components/SearchItem";
    export default {
        name:'Result',
        components:{SearchItem},
        computed:{
            eltitle(){return this.$t('msg.notice')}
        },
        data(){
            return{
                dialogVisible2:false,
                ans:'',
                ansid:'',
                res:[],
            }
        },
        methods:{
            eventget(str){
                this.$axios.get('http://47.95.199.35:8000/search',{
                    params: {q:str}
                }).then((response) => {
                    console.log(response.data)
                    if(response.data.count > 0){
                        this.res = response.data.res
                    }
                }).catch(() => {

                });
            },
            addA(id){
                this.dialogVisible2 = true
                this.ansid = id
            },
            addans(){
                this.$axios.get("http://47.95.199.35:8000/ansques",{
                    params:{id:this.ansid,ans:this.ans}
                }).then((response)=>{
                    if(response.status==200){
                        this.$message(this.$t('msg.adda')+this.$t('msg.success'));
                        this.reload()
                    }
                }).catch(()=>{
                })
                this.dialogVisible2=false
            }
        },
        created:function () {
            this.eventget(this.$route.params.title)
        }
    }
</script>

<style scoped>
    .searchBox{
        margin-top: 10px;
        margin-left: 20px;
        margin-bottom: 20px;
        width: 80%;
    }
    .test{
        width: 80%;
        margin-left: 20px;
        margin-top: 10px;
    }
    #left{
        float: left;
        width: 70%;
    }
    #left-in{
        font-size: 10px;
        float: left;
        width: 90%;
    }
    #right{
        margin-top:5px;
        margin-bottom: 5px;
        float: right;
        width: 10%;
    }
    .my-col-item >>> .el-collapse-item__header{
        font-size: 14px;
    }
</style>