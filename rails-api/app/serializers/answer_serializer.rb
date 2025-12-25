class AnswerSerializer
  def initialize(data)
    @data = data
  end

  def serialized_json
    {
      answer: @data["answer"],
      confidence: @data["confidence"]
    }
  end
end
