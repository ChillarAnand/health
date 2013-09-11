// Copyright (c) 2013, Web Notes Technologies Pvt. Ltd.
// License: GNU General Public License v3. See license.txt

if(!window.erpnext) erpnext = {};

// Add / update a new Lead / Communication
// subject, sender, description
erpnext.send_message = function(opts) {
	return wn.call({
		type: "POST",
		method: "selling.utils.contact.send_message",
		args: opts,
		callback: opts.callback
	});
}

// Setup the user tools
//
$(document).ready(function() {
	// update login
	erpnext.cart.set_cart_count();
	
	$("#user-tools a").tooltip({"placement":"bottom"});
	$("#user-tools-post-login a").tooltip({"placement":"bottom"});
});

// shopping cart
if(!erpnext.cart) erpnext.cart = {};

$.extend(erpnext.cart, {
	update_cart: function(opts) {
		if(!full_name) {
			if(localStorage) {
				localStorage.setItem("last_visited", window.location.href.split("/").slice(-1)[0]);
				localStorage.setItem("pending_add_to_cart", opts.item_code);
			}
			window.location.href = "login";
		} else {
			return wn.call({
				type: "POST",
				method: "selling.utils.cart.update_cart",
				args: {
					item_code: opts.item_code,
					qty: opts.qty,
					with_doclist: opts.with_doclist
				},
				btn: opts.btn,
				callback: function(r) {
					if(opts.callback)
						opts.callback(r);
					
					erpnext.cart.set_cart_count();
				}
			});
		}
	},
	
	set_cart_count: function() {
		var cart_count = getCookie("cart_count");
		var $cart = $("#website-post-login").find('[data-label="Cart"]');
		var $badge = $cart.find(".badge");
		var $cog = $("#website-post-login").find(".dropdown-toggle");
		var $cog_count = $cog.find(".cart-count");
		if(cart_count) {
			if($badge.length === 0) {
				var $badge = $('<span class="badge pull-right"></span>').appendTo($cart.find("a"));
			}
			$badge.html(cart_count);
			if($cog_count.length === 0) {
				var $cog_count = $('<sup class="cart-count"></span>').insertAfter($cog.find(".icon-cog"));
			}
			$cog_count.html(cart_count);
		} else {
			$badge.remove();
			$cog_count.remove();
		}
	}
});