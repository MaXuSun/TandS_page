<template>
    <div id="signup">
        <div class="body">
            <div class="title">
                <router-link to="/user/signin" class="in">{{$t('user.signin')}}</router-link>
                <span>·</span>
                <router-link to="/user/signup" class="up">{{$t('user.signup')}}</router-link>
            </div>
            <div class="content">
                <div class="input">
                    <el-input
                            :placeholder=elinputname
                            prefix-icon="el-icon-user"
                            clearable
                            v-model="user.name">
                    </el-input>
                </div>
                <div class="input">
                    <el-input
                            :placeholder=elinputphone
                            prefix-icon="el-icon-phone"
                            clearable
                            v-model="user.phone">
                    </el-input>
                </div>
                <div class="input">
                    <el-input
                            :placeholder=elinputkey
                            prefix-icon="el-icon-lock"
                            show-password
                            v-model="user.pwd">
                    </el-input>
                </div>
                <div class="tip">
                    <el-link type="info" :underline="false" @click="$i18n.locale=='en'?$i18n.locale='zh':$i18n.locale='en'">{{$t('language.switch')}}</el-link>
                </div>
                <div class="button">
                    <el-button type="primary" @click="signUp">{{$t('user.signup')}}</el-button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "SignUp",
        data() {
            return {
                user: {
                    name: '',
                    phone: '',
                    pwd: '',
                },
            }
        },
        computed:{
            elinputphone(){return this.$t('msg.phonenumber')},
            elinputkey(){return this.$t('msg.keyword')},
            elinputname(){return this.$t('msg.name')}
        },
        methods: {
            signUp() {
                // 数据验证
                let name_reg = /^[\u4E00-\u9FA5\uF900-\uFA2D|\w]{1,20}$/;
                if (!name_reg.test(this.user.name)) {
                    this.$message.error('昵称不能为空或含特殊字符');
                    return;
                }
                let phone_reg = /^1[3456789]\d{9}$/;
                if (!phone_reg.test(this.user.phone)) {
                    this.$message.error('请输入有效的手机号');
                    return;
                }
                let password_reg = /^(\w){4,20}$/;
                if (!password_reg.test(this.user.password)) {
                    this.$message.error('密码得是6-20位的字母和数字');
                    return;
                }
                // 网络传输
                this.$axios.get('http://47.95.199.35:8000/register', {
                    params: this.user
                }).then((response) => {
                    if(response.status==200) {
                        this.user.name = "";//置空
                        this.user.phone = "";//置空
                        this.user.pwd = "";//置空
                        this.$router.replace({
                            path: '/user/signin',
                        });
                        var msg= this.$t('user.signupsuc')
                        this.$message.success(msg);
                    }
                }).catch(() => {
                });
            }
        }
    }
</script>

<style scoped>
    #signup {
        border-radius: 4px;
        box-shadow: 0 0 8px rgba(0, 0, 0, .1);
    }

    .body {
        padding: 50px 50px 50px;
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

    .title .up {
        padding: 10px;
        color: #4d79dd;
        font-size: 18px;
        text-decoration: none;
        border-bottom: 2px solid #4d79dd;
    }

    .title .in {
        padding: 10px;
        color: #A9BDDE;
        font-size: 18px;
        text-decoration: none;
    }

    .title .in:hover {
        border-bottom: 2px solid #4d79dd;
    }

    .content {
        margin-top: 40px;
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