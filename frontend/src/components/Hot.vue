<template>
    <div>
        <el-tag
                v-for="(item,index) in items"
                :key="index"
                :type="item.type"
                @click.native="gethot(item.label)"
                effect="plain">
<!--            <i class="el-icon-user-solid"></i>-->
            {{ item.label }}
        </el-tag>
    </div>
</template>

<script>
    export default {
        name: "Hot",
        data(){
            return{
                items: [
                    { type: 'info', label: 'Loading' },
                    { type: 'info', label: 'Loading' },
                    { type: 'info', label: 'Loading' },
                    { type: 'info', label: 'Loading' },
                    { type: 'info', label: 'Loading' }
                ]
            }
        },
        mounted:function () {
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
    .el-tag{
        font-size: 16px;
        margin-left: 5%;
        margin-top: 3%;
        margin-bottom: 5%;
    }
</style>