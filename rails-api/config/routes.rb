Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      post "/questions", to: "questions#create"
      get "/auth/shopify/callback", to: "auth#callback"
    end
  end
end
