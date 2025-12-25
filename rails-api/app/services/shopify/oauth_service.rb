module Shopify
  class OauthService
    def self.exchange_token(shop, code)
      response = Faraday.post(
        "https://#{shop}/admin/oauth/access_token",
        {
          client_id: ENV["SHOPIFY_API_KEY"],
          client_secret: ENV["SHOPIFY_API_SECRET"],
          code: code
        }
      )

      JSON.parse(response.body)["access_token"]
    end
  end
end
