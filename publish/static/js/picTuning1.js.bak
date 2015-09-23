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
	 			ratio = $(left).attr("alt");
		 		// width = $(left).width(),
		 		// height = $(left).height(),
		 		// ratio = width / height;	

		 	if($(left).hasClass("done")) return;

	 		if(ratio <= 0.6){
	 			$(left).width(220);
	 			$(left).parent().width(220);
	 		}
	 		if(ratio > 0.6  &&  ratio <= 0.7){
	 			$(left).width(260);
	 			$(left).parent().width(260);
	 		}
	 		if(ratio > 0.7  &&  ratio <= 0.8){
	 			$(left).width(290);
	 			$(left).parent().width(290);
	 		}
	 		if(ratio > 0.8  &&  ratio < 1){
	 			$(left).width(310);
	 			$(left).parent().width(310);
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

		 	if($(left).hasClass("done")) return;
		 	if($(right).hasClass("done")) return;

		 	$(right).width(width);
		 	$(right).parent().width(outerWidth);		 	

		 	self.cutMargin(left,right);
	 	},



	 	cutMargin : function(left,right){
	 		$(left).css({"height":"auto"});
		 	$(right).css({"height":"auto"});

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

	 		$(left).addClass("done");
	 		$(right).addClass("done");

	 	}  	

	};

	return tuning;

}