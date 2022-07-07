<template>
	<div>
		<form @submit.prevent="update_data">
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
			<button v-on:click="button">更新</button>
		</form>
		<hr />
		<h2><p>{{error_message}}</p></h2>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	data() {
		return {
			error_message: ''
		}
	},
	methods: {
		update_data() {
			axios.put('http://127.0.0.1:5000/user/update', {
				email: this.email,
				stock_name: this.stock,
				target_price: this.price
			})
			.then(res => {
				console.log(res);
				this.error_message = '更新成功';
			})
			.catch(error =>{
				if(error.response){
					if (error.response.status == 400){
						this.error_message = '請檢查信箱與股票名稱是否有誤';
					}else if(error.response.status == 406){
						this.error_message = '請填入所有的資料';
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
