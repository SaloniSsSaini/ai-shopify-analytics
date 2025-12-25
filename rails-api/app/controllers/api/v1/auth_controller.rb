module Api
  module V1
    class AuthController < ApplicationController
      def callback
        token = Shopify::OauthService.exchange_token(
          params[:shop],
          params[:code]
        )

        Store.find_or_create_by(shop_domain: params[:shop])
             .update!(access_token: token)

        render json: { success: true }
      end
    end
  end
end
