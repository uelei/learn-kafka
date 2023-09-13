package main

import (
     "fmt"
     "log"
     "time"

     "github.com/IBM/sarama"
)

func main() {
     // Define the Kafka broker addresses.
     brokerList := []string{"localhost:19092"}

     // Create a Kafka producer configuration.
     config := sarama.NewConfig()
     config.Producer.Return.Successes = true

     // Create a Kafka producer.
     producer, err := sarama.NewSyncProducer(brokerList, config)
     if err != nil {
          log.Fatalf("Error creating producer: %v", err)
     }
     defer func() {
          if err := producer.Close(); err != nil {
               log.Fatalf("Error closing producer: %v", err)
          }
     }()

     // Define the Kafka topic you want to produce to.
     topic := "vaifilhao"

     // Create a loop to continuously produce messages.
     for i := 0; ; i++ {
          message := fmt.Sprintf("Message %d - %s", i, time.Now().Format(time.RFC3339))
          // Create a Kafka message.
          kafkaMessage := &sarama.ProducerMessage{
               Topic: topic,
               Value: sarama.StringEncoder(message),
          }

          // Send the message to Kafka and handle any errors.
          _, _, err := producer.SendMessage(kafkaMessage)
          if err != nil {
               log.Printf("Error sending message: %v", err)
          } else {
               log.Printf("Sent: %s", message)
          }

          // Sleep for some time before sending the next message.
          time.Sleep(1 * time.Second)
     }
}
