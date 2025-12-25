class AiServiceClient
  def self.ask(store, question)
    response = Faraday.post(
      ENV["AI_SERVICE_URL"],
      {
        store_id: store.shop_domain,
        question: question,
        token: store.access_token
      }.to_json,
      { "Content-Type" => "application/json" }
    )

    JSON.parse(response.body)
  end
end
