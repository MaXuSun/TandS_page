<template>
    <div id="signin">
        <div class="body">
            <div class="title">
                <router-link to="/user/signin" class="in">{{$t('user.signin')}}</router-link>
                <span>·</span>
                <router-link to="/user/signup" class="up">{{$t('user.signup')}}</router-link>
            </div>
            <div class="content">
                <div class="input">
                    <el-input
                            :placeholder=elinputphone
                            prefix-icon="el-icon-message"
                            clearable
                            v-model="user.phone">
                    </el-input>
                </div>
                <div class="input">
                    <el-input
                            :placeholder=elinputkey
                            prefix-icon="el-icon-lock"
                            show-password
                            v-model="user.password">
                    </el-input>
                </div>
                <div class="tip">
                    <el-link type="info" :underline="false" @click="$i18n.locale=='en'?$i18n.locale='zh':$i18n.locale='en'">{{$t('language.switch')}}</el-link>
                </div>
                <div class="button">
                    <el-button type="primary" @click="signIn" :loading="loading">{{$t('user.signin')}}</el-button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "SignIn",
        data() {
            return {
                user: {
                    phone: '',
                    password: '',
                },
                loading: false,
            }
        },
        computed:{
            elinputphone(){return this.$t('msg.phonenumber')},
            elinputkey(){return this.$t('msg.keyword')},
        },
        methods: {
            signIn() {
                // 数据验证
                // let phone_reg = /^1[3456789]\d{9}$/;
                // if (!phone_reg.test(this.user.phone)) {
                //     this.$message.error('请输入有效的手机号');
                //     return;
                // }
                // let password_reg = /^(\w){6,20}$/;
                // if (!password_reg.test(this.user.password)) {
                //     this.$message.error('密码得是6-20位的字母和数字');
                //     return;
                // }
                // this.loading = true;//按钮不可操作
                // // 网络传输
                // this.$axios.get(this.api.usersAccountAPI, {
                //     params: this.user
                // }).then((response) => {
                //     if (response.data.code === 200) {
                //         //在本地保存登录记录
                //         this.$cookies.set('token', response.data.data.token, 60 * 60 * 24 * 30);
                //         this.$cookies.set('user', response.data.data.user, 60 * 60 * 24 * 30);
                //         // 配置全局token和user
                //         this.$axios.defaults.headers.common['token'] = response.data.data.token;
                //         this.api.user = response.data.data.user;
                //         //置空
                //         this.user.phone = "";//置空
                //         this.user.password = "";//置空
                //         // 消息提示
                //         this.$message.success('登录成功，正在同步数据');
                //         //跳转
                //         this.$router.push({
                //             path: '/',
                //         });
                //     } else {//只能是手机号或密码不对
                //         this.$message.error('手机号或密码有误');
                //     }
                //     this.loading = false;//按钮可操作
                // }).catch(() => {
                //     this.loading = false;//按钮可操作
                // });
                this.$router.replace('/index')
            }
        }
    }
</script>

<style scoped>

    #signin {
        border-radius: 4px;
        box-shadow: 0 0 8px rgba(0, 0, 0, .1);
    }

    .head span {
        color: #ffffff;
    }

    .body {
        padding: 50px 50px 70px;
        background-color: #545C64;
        border: 2px solid #545C64;
    }


    .title {
        text-align: center;
    }

    .title span {
        font-size: 18px;
        padding: 10px;
        color: #A9BDDE;
        font-weight: bold;
    }

    .title .in {
        padding: 10px;
        color: #4d79dd;
        font-size: 18px;
        text-decoration: none;
        border-bottom: 2px solid #4d79dd;
    }

    .title .up {
        padding: 10px;
        color: #A9BDDE;
        font-size: 18px;
        text-decoration: none;
    }

    .title .up:hover {
        border-bottom: 2px solid #4d79dd;
    }

    .content {
        margin-top: 60px;
    }

    .content .input {
        margin-top: 10px;
    }

    .content .tip {
        margin-top: 10px;
        text-align: right;
    }

    .content .button {
        margin-top: 25px;
    }

    .content .button >>> .el-button--primary {
        width: 100%;
    }
</style>