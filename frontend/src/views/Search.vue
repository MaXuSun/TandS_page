<template>
    <div class="box">
            <div class="searchBox">
                <search-item></search-item>
            </div>
            <div class="searchBox2">
                <SearchHot @childevent="gethot"></SearchHot>
            </div>
    </div>
</template>

<script>
    import SearchItem from "@/components/SearchItem";
    import SearchHot from "@/components/SearchHot";
    export default {
        name: "Search",
        components: {SearchItem,SearchHot},
        computed:{
            elinputplace(){return this.$t('msg.searchkey')},
        },
        data(){
          return{
              items: [
                  { type: '', label: '标签一' },
                  { type: 'success', label: '标签二' },
                  { type: 'info', label: '标签三' },
                  { type: 'danger', label: '标签四' },
                  { type: 'warning', label: '标签五' }
              ]
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
                console.log("dsfas")
                this.$router.replace('/index/result/'+label)
            }
        }
    }
</script>

<style>
    .box{
        margin: 5% auto;
        padding-top: 6%;
        height: 60px;
        width: 100%;
    }
    .searchBox{
        margin: 0 auto;
        width: 60%;
        position: relative;
    }
    .searchBox2{
        margin: 0 auto;
        width: 60%;
        position: relative;
    }
</style>