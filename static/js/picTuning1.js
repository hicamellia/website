function PicTuning(selector){

	var tuning = {

	 	init : function(){
	 		var self = this;
	 		self.getPic();
	 	},

	 	getPic : function(){
	 		var self = this,
	 			left = '',
	 			right = '';

	 		$(selector).each(function(i){
	 			if(i % 2 == 0){
	 				left = this;
	 				self.doLeft(left);
	 			}
	 			if(i % 2 == 1){
	 				right = this;
	 				self.doRight(left,right);
	 			}
	 		});
	 	},

	 	doLeft : function(left){
	 		var self = this,
		 		width = $(left).width(),
		 		height = $(left).height(),
		 		ratio = width / height;	

	 		if(ratio <= 0.5){
	 			$(left).width(110);
	 			$(left).parent().width(110);
	 		}
	 		if(ratio > 0.5  &&  ratio < 1){
	 			$(left).width(140);
	 			$(left).parent().width(140);
	 		}
	 		if(ratio >= 1){
	 			$(left).width("100%");
	 			$(left).parent().width("95%");
	 		}
	 	},

	 	doRight : function(left,right){
	 		var self = this,
		 		width = $(left).width(),
		 		outerWidth = $(left).parent().width();
		 	$(right).width(width);
		 	$(right).parent().width(outerWidth);

		 	self.cutMargin(left,right);
	 	},



	 	cutMargin : function(left,right){
	 		var lHeight = $(left).height(),
	 			rHeight = $(right).height();
	 		if(lHeight < rHeight){ 
	 			$(left).height(rHeight);
	 			$(right).height(rHeight); 
	 		}
	 		if(rHeight < lHeight){
	 			$(right).height(lHeight); 
	 			$(left).height(lHeight);
	 		}
	 	}  	

	};

	return tuning;

}
