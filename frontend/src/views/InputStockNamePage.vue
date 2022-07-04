<template>
	<div>
		<form @submit.prevent="create_user">
			<h2>
				<label for="user">姓名:&nbsp;&nbsp;&nbsp;</label>
				<input id="user" type="text" v-model.trim="user" />
			</h2>
			<h2>
				<label for="email">信箱:&nbsp;&nbsp;&nbsp;</label>
				<input id="email" type="text" v-model.trim="email" />
			</h2>
			<h2>
				<label for="stock">股票:&nbsp;&nbsp;&nbsp;</label>
				<input id="stock" type="text" v-model.trim="stock" />
			</h2>
			<h2>
				<label for="price">價錢:&nbsp;&nbsp;&nbsp;</label>
				<input id="price" type="text" v-model.trim="price" />
			</h2>
			<button v-on:click="button">提交</button>
		</form>
		<hr />
		<h2><p>{{create}}</p></h2>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	data() {
		return {
			create: "",
		};
	},
	methods: {
		create_user() {
			axios.post('http://127.0.0.1:5000/user/create', {
				username:this.user,
				email: this.email,
				stock_name: this.stock,
				target_price: this.price
			})
			.then(res => {
				console.log(res);
				this.create = '創建成功';
			})
			.catch(error =>{
				if(error.response){
					if (error.response.status == 400){
						this.create = '請輸入正確的股票名稱';
					}else if(error.response.status == 406){
						this.create = '請填入所有的資料';
					}
				}else if(error.request){
					alert("沒有收到回應");
				}else{
					alert("伺服器請求失敗");
				}
			})
		},
	},
};
</script>
