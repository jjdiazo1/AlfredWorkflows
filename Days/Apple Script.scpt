FasdUAS 1.101.10   ��   ��    k             i         I      �� 	���� (0 viewcalendarforday viewCalendarForDay 	  
�� 
 o      ���� 0 dayindex dayIndex��  ��    k     i       l     ��  ��       Obtenemos la fecha actual     �   4   O b t e n e m o s   l a   f e c h a   a c t u a l      r         I    ������
�� .misccurdldt    ��� null��  ��    o      ���� 	0 today        l   ��  ��    P J Calculamos el d�a de la semana actual (0 para lunes, 1 para martes, etc.)     �   �   C a l c u l a m o s   e l   d � a   d e   l a   s e m a n a   a c t u a l   ( 0   p a r a   l u n e s ,   1   p a r a   m a r t e s ,   e t c . )      r        c        n       !   m   	 ��
�� 
wkdy ! o    	���� 	0 today    m    ��
�� 
long  o      ���� 0 todayweekday todayWeekday   " # " l    $ % & $ r     ' ( ' \     ) * ) o    ���� 0 todayweekday todayWeekday * m    ����  ( o      ���� 0 todayweekday todayWeekday % F @ Ajustamos porque AppleScript cuenta desde domingo (domingo = 1)    & � + + �   A j u s t a m o s   p o r q u e   A p p l e S c r i p t   c u e n t a   d e s d e   d o m i n g o   ( d o m i n g o   =   1 ) #  , - , l   ��������  ��  ��   -  . / . Z    % 0 1���� 0 A     2 3 2 o    ���� 0 todayweekday todayWeekday 3 m    ����   1 r    ! 4 5 4 [     6 7 6 o    ���� 0 todayweekday todayWeekday 7 m    ����  5 o      ���� 0 todayweekday todayWeekday��  ��   /  8 9 8 l  & &��������  ��  ��   9  : ; : l  & &�� < =��   < : 4 Calculamos los d�as hasta el pr�ximo d�a solicitado    = � > > h   C a l c u l a m o s   l o s   d � a s   h a s t a   e l   p r � x i m o   d � a   s o l i c i t a d o ;  ? @ ? r   & + A B A l  & ) C���� C \   & ) D E D o   & '���� 0 dayindex dayIndex E o   ' (���� 0 todayweekday todayWeekday��  ��   B o      ���� 0 daysuntilnext daysUntilNext @  F G F Z   , ; H I���� H A   , / J K J o   , -���� 0 daysuntilnext daysUntilNext K m   - .����   I r   2 7 L M L [   2 5 N O N o   2 3���� 0 daysuntilnext daysUntilNext O m   3 4����  M o      ���� 0 daysuntilnext daysUntilNext��  ��   G  P Q P l  < <��������  ��  ��   Q  R S R l  < <�� T U��   T 5 / Calculamos la fecha del pr�ximo d�a solicitado    U � V V ^   C a l c u l a m o s   l a   f e c h a   d e l   p r � x i m o   d � a   s o l i c i t a d o S  W X W r   < C Y Z Y [   < A [ \ [ o   < =���� 	0 today   \ l  = @ ]���� ] ]   = @ ^ _ ^ o   = >���� 0 daysuntilnext daysUntilNext _ 1   > ?��
�� 
days��  ��   Z o      ���� 0 nextdate nextDate X  ` a ` l  D D��������  ��  ��   a  b c b l  D D�� d e��   d 3 - Abrimos el calendario en la fecha solicitada    e � f f Z   A b r i m o s   e l   c a l e n d a r i o   e n   l a   f e c h a   s o l i c i t a d a c  g�� g O   D i h i h k   H h j j  k l k I  H O���� m
�� .wrbtaec9null��� ��� null��   m �� n��
�� 
wtdt n o   J K���� 0 nextdate nextDate��   l  o p o l  P U q r s q I  P U�� t��
�� .sysodelanull��� ��� nmbr t m   P Q���� ��   r C = Espera un momento para que se cargue la vista del calendario    s � u u z   E s p e r a   u n   m o m e n t o   p a r a   q u e   s e   c a r g u e   l a   v i s t a   d e l   c a l e n d a r i o p  v w v l  V [ x y z x I  V [������
�� .miscactvnull��� ��� null��  ��   y 5 / Asegura que la aplicaci�n est� en primer plano    z � { { ^   A s e g u r a   q u e   l a   a p l i c a c i � n   e s t �   e n   p r i m e r   p l a n o w  |�� | O   \ h } ~ } l  ` g  � �  I  ` g�� � �
�� .prcskprsnull���     ctxt � m   ` a � � � � �  1 � �� ���
�� 
faal � m   b c��
�� eMdsKcmd��   � ) # Cambia a la vista de d�a (Cmd + 1)    � � � � F   C a m b i a   a   l a   v i s t a   d e   d � a   ( C m d   +   1 ) ~ m   \ ] � ��                                                                                  sevs  alis    \  Macintosh HD               �!:3BD ����System Events.app                                              �����!:3        ����  
 cu             CoreServices  0/:System:Library:CoreServices:System Events.app/  $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��  ��   i m   D E � ��                                                                                  wrbt  alis    8  Macintosh HD               �!:3BD ����Calendar.app                                                   �����!:3        ����  
 cu             Applications  #/:System:Applications:Calendar.app/     C a l e n d a r . a p p    M a c i n t o s h   H D   System/Applications/Calendar.app  / ��  ��     � � � l     ��������  ��  ��   �  � � � l     �� � ���   � ^ X Llamada al script con el d�a de la semana como variable (por ejemplo, 2 para mi�rcoles)    � � � � �   L l a m a d a   a l   s c r i p t   c o n   e l   d � a   d e   l a   s e m a n a   c o m o   v a r i a b l e   ( p o r   e j e m p l o ,   2   p a r a   m i � r c o l e s ) �  ��� � l     ����� � I     �� ����� (0 viewcalendarforday viewCalendarForDay �  ��� � m    ����  ��  ��  ��  ��  ��       �� � � ���   � ������ (0 viewcalendarforday viewCalendarForDay
�� .aevtoappnull  �   � **** � �� ���� � ����� (0 viewcalendarforday viewCalendarForDay�� �� ���  �  ���� 0 dayindex dayIndex��   � ������������ 0 dayindex dayIndex�� 	0 today  �� 0 todayweekday todayWeekday�� 0 daysuntilnext daysUntilNext�� 0 nextdate nextDate � ���������� ��������� � �������
�� .misccurdldt    ��� null
�� 
wkdy
�� 
long�� 
�� 
days
�� 
wtdt
�� .wrbtaec9null��� ��� null
�� .sysodelanull��� ��� nmbr
�� .miscactvnull��� ��� null
�� 
faal
�� eMdsKcmd
�� .prcskprsnull���     ctxt�� j*j  E�O��,�&E�O�lE�O�j 
��E�Y hO��E�O�j 
��E�Y hO��� E�O� "*�l Okj O*j 	O� 	���l UU � �� ����� � ���
�� .aevtoappnull  �   � **** � k      � �  �����  ��  ��   �   � ���� (0 viewcalendarforday viewCalendarForDay�� *jk+  ascr  ��ޭ