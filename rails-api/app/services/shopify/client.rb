module Shopify
  class Client
    def initialize(store)
      @store = store
    end

    def graphql(query)
      Faraday.post(
        "https://#{@store.shop_domain}/admin/api/2024-01/graphql.json",
        { query: query }.to_json,
        {
          "X-Shopify-Access-Token" => @store.access_token,
          "Content-Type" => "application/json"
        }
      )
    end
  end
end
