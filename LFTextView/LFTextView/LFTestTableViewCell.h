//
//  LFTestTableViewCell.h
//  LFTextView
//
//  Created by 刘飞 on 2017/8/16.
//  Copyright © 2017年 刘飞. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface LFTestTableViewCell : UITableViewCell

+(UINib *)Nib;///<作注册只用


@property (nonatomic, strong) UILabel *titleLabel;
@property (nonatomic, strong) UILabel *subtitleLabel;




@end
