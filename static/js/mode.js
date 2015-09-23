//大图相应样式尺寸
function Pic_sizer(parent,ratioX,ratioY){

	var sizer = {

		init : function(){
			var self = this;
			self.render();
			self.bind_resize();			
		},

		bind_resize : function(){
			var self = this;
			$(window).resize(function(){
				self.render();
			});
		},

		render : function(){
			var width = $(parent).width(),
				height = parseInt(width/ratioX) * ratioY,
				children = $(parent).children("img");
			$(parent).css({"height":height});
			children.css({"width":width});
			if(children.css("height")<height){
				children.css({"height":height});
			}
			

		}
	};

	return sizer;
}


//加载数据
function Render_data(){

	var flag = "open";

	var count = 0;

	var rendering = {

		init : function(){
			var self = this;			
			self.bind_trigger();
		},

		bind_trigger : function(){
			var self = this;	
			$(window).scroll(function(){	
				var _document = $(document.body).height(),
					_scroll = $(window).scrollTop(),
					_window = $(window).height(),
					margin = _document - _scroll - _window;			
			    if(margin < 4){

			    	//检测阀门
					if(flag == "closed") return;

					//暂时关闭阀门
					flag = "closed";

			    	self.ajax_request();
			    }
			});
		},

		ajax_request : function(){
			var self = this,
				start = parseInt($("#items_start").val()),
				length = parseInt($("#items_length").val()),
				id = parseInt($("#topic_id").val()),
				// u = "../json/mode.json";
				//u = "../json/test1.json";				
				u = "../topic_api";
			
			start = start + length * count;
			count++;
			u = u+"?id="+id+"&start="+start+"&length="+length;

			$.ajax({
				url : u,
				dataType : "json",
				success : function(data){
					if(data.items.length) self.do_render(data);
					else self.no_more();
				}
			});
		},

		do_render : function(data){
			var self = this,
				template = '{{#items}}<div class="entry added"><a class="spic_wrap" href="{{url}}" target="_blank"><div class="spic_box"><img src="{{image_entity}}" alt="{{ratio}}"/></div></a><div class="info ellipsis"><div class="brand">{{brand}}</div><div class="name">{{title}}</div></div><div class="sep"></div><div class="price"><span class="new">{{sell_price}} {{currency}}</span>{{#is_discount}}<span class="old">{{original_price}} {{currency}}<span>{{/is_discount}}</div><a class="url" href="http://{{site}}" target="_blank">{{site}}</a><div class="buy">点击购买</div>{{#is_discount}}<div class="sale"></div>{{/is_discount}}</div>{{/items}}',
				node = Mustache.render(template,data);
					
			$("#content").append(node);

			//重新开启阀门
			flag = "open";
			
		},

		no_more : function(){
			$(".spin_box").hide();
			$(".no_more").show();

			//永久关闭阀门
			flag = "closed";
		}

	};

	return rendering;


}