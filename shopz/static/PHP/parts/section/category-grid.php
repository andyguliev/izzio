	<?php 
		$products = array(
			array(
				'product_name' => 'Sony Ericson Vaga',
				'is_new' => true,
				'is_sale' =>false,
				'is_hot' =>false,
				'productImageURL' => 'assets/images/products/c1.jpg'


				),
			array(
				'product_name' => 'Samsung Galaxy S4',
				'is_new' => false,
				'is_sale' =>true,
				'is_hot' =>false,
				'productImageURL' => 'assets/images/products/c2.jpg'



				),
			array(
				'product_name' => 'Samsung Galaxy S4',
				'is_new' => false,
				'is_sale' =>false,
				'is_hot' =>true,
				'productImageURL' => 'assets/images/products/c3.jpg'


				),
			array(
				'product_name' => 'Apple Iphone 5s 32GB',
				'is_new' => false,
				'is_sale' =>false,
				'is_hot' =>true,
				'productImageURL' => 'assets/images/products/c4.jpg'


				),
			array(
				'product_name' => 'Nokia',
				'is_new' => false,
				'is_sale' =>true,
				'is_hot' =>false,
				'productImageURL' => 'assets/images/products/c5.jpg'


				),
			array(
				'product_name' => 'Nokia',
				'is_new' => true,
				'is_sale' =>false,
				'is_hot' =>false,
				'productImageURL' => 'assets/images/products/c6.jpg'


				),
			array(
				'product_name' => 'Sony Ericson Vaga',
				'is_new' => true,
				'is_sale' =>false,
				'is_hot' =>false,
				'productImageURL' => 'assets/images/products/c4.jpg'

				),
			array(
				'product_name' => 'Samsung Galaxy S4',
				'is_new' => false,
				'is_sale' =>true,
				'is_hot' =>false,
				'productImageURL' => 'assets/images/products/c2.jpg'



				),
			array(
				'product_name' => 'Samsung Galaxy S4',
				'is_new' => false,
				'is_sale' =>false,
				'is_hot' =>true,
				'productImageURL' => 'assets/images/products/c1.jpg'


				),
			array(
				'product_name' => 'Sony Ericson Vaga',
				'is_new' => true,
				'is_sale' =>false,
				'is_hot' =>false,
				'productImageURL' => 'assets/images/products/c6.jpg'


				),
			array(
				'product_name' => 'Samsung Galaxy S4',
				'is_new' => false,
				'is_sale' =>true,
				'is_hot' =>false,
				'productImageURL' => 'assets/images/products/c5.jpg'



				),
			array(
				'product_name' => 'Samsung Galaxy S4',
				'is_new' => false,
				'is_sale' =>false,
				'is_hot' =>true,
				'productImageURL' => 'assets/images/products/c3.jpg'



				)
			);
		foreach($products as $product):
			?>

		<div class="col-sm-6 col-md-4 wow fadeInUp">
			<div class="products">
				<?php displayProduct($product['product_name'], $product['is_new'],$product['is_sale'],$product['is_hot'],$product['productImageURL']) ; ?>
			</div><!-- /.products -->
		</div><!-- /.item -->
	<?php endforeach;?>
	