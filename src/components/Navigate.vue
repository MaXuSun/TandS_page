<template>
    <div id="navigate">
        <el-menu class="menu_left"
                :default-active="this.$route.path"
                mode="horizontal"
                background-color="#545c64"
                text-color="#fff"
                active-text-color="#ffd04b">
            <el-submenu index="6">
                <template slot="title">{{$t('user.logout')}}</template>
                <el-menu-item index="5-1" @click="logoutClick">{{$t('other.logout')}}</el-menu-item>
                <el-menu-item index="5-2" @click="changeClick">{{$t('user.changeuser')}}</el-menu-item>
            </el-submenu>
            <el-menu-item index="1" @click="schClick">{{$t('other.schedule')}}</el-menu-item>
            <el-menu-item index="3" >{{$t('other.policy')}}</el-menu-item>
            <el-menu-item index="4">
                <el-input
                        :placeholder=elinputplace
                        prefix-icon="el-icon-search"/>
            </el-menu-item>
        </el-menu>
        <el-menu class="menu_right"
                 mode="horizontal"
                 background-color="#545c64"
                 text-color="#fff"
                 active-text-color="#ffd04b">
            <el-submenu index="5">
                <template slot="title">{{$t('language.language')}}</template>
                <el-menu-item index="5-1" @click="changeZh">{{$t('language.zh')}}</el-menu-item>
                <el-menu-item index="5-2" @click="changeEng">{{$t('language.en')}}</el-menu-item>
            </el-submenu>
        </el-menu>
        <el-dialog
                :title=eltitle
                :visible.sync="dialogVisible"
                width="30%">
            <span>{{message}}</span>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">{{$t('msg.cancel')}}</el-button>
                <el-button type="primary" @click="okclick">{{$t('msg.yes')}}</el-button>
          </span>
        </el-dialog>
    </div>
</template>

<script>
    export default {
        name: "Navigate",
        data(){
          return{
              dialogVisible:false,
              message:'',
          }
        },
        computed:{
            elinputplace(){return this.$t('msg.searchkey')},
            eltitle(){return this.$t('msg.notice')},
        },
        methods:{
            // 查看课表
            schClick(){
                this.$router.replace("/index/schedule")
            },

            // 退出或者切换账户
            // 退出按钮
            logoutClick(){
                this.message = this.$t('msg.logout')
                this.dialogVisible = true
            },
            // 切换账号
            changeClick(){
                this.message = this.$t('msg.changeuser')
                this.dialogVisible = true
            },
            // 确认退出或者切换账户
            okclick(){
                this.dialogVisible = false
                if(this.message == this.$t('msg.changeuser')){
                    this.$router.replace('/user/signin')
                }else  if(this.message == this.$t('msg.logout')){
                    this.$router.replace('/user/logout')
                }
            },

            // 选择语言
            // 选择英语
            changeEng(){
                this.$i18n.locale = 'en'
            },
            // 选择中文
            changeZh(){
                this.$i18n.locale='zh'
            }
        }
    }
</script>

<style scoped>
#navigate {
    width: 100%;
    background-color: #545C64;
    display: inline-block;
    border-bottom: none;
}
#navigate >>> .el-menu.el-menu--horizontal {
    border-bottom:none;
    display: inline-block;
}
.menu_left{

}
.menu_right{
    float: right;
}
</style>