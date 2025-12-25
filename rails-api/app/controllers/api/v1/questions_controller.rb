# placeholder
module Api
  module V1
    class QuestionsController < ApplicationController
      def create
        store = Store.find_by(shop_domain: params[:store_id])
        return render json: { error: "Store not found" }, status: 404 unless store

        ai_response = AiServiceClient.ask(store, params[:question])

        store.question_logs.create!(
          question: params[:question],
          answer: ai_response["answer"]
        )

        render json: AnswerSerializer.new(ai_response).serialized_json
      end
    end
  end
end
